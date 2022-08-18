from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
import datetime

## Delete this code:
# import requests
# posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    # body = StringField("Blog Content", validators=[DataRequired()])
    body = CKEditorField('Body')
    submit = SubmitField("Submit Post")
posts = db.session.query(BlogPost).all()

@app.route('/')
def get_all_posts():
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    posts = db.session.query(BlogPost).all()
    print(index)
    requested_post = None
    for blog_post in posts:
        if blog_post.id == index:
            requested_post = blog_post
    print(requested_post.title)
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/new-post", methods=["GET", "POST"])
def create_new_post():
    form = CreatePostForm()
    if request.method == "GET":
        return render_template("make-post.html", form=form, new=True)
    elif request.method == "POST":
        if form.validate_on_submit():
            new_blog_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            date=datetime.datetime.now().strftime("%B %d,%Y"),
            body=form.body.data,
            author=form.author.data,
            img_url=form.img_url.data
            )
            db.session.add(new_blog_post)
            db.session.commit()
            posts = db.session.query(BlogPost).all()
            return redirect(url_for("get_all_posts"))

@app.route("/edit-post/<post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    print(post_id)
    post_to_update = BlogPost.query.get(post_id)
    form = CreatePostForm(
        title=post_to_update.title,
        subtitle=post_to_update.subtitle,
        img_url=post_to_update.img_url,
        author=post_to_update.author,
        body=post_to_update.body,
        submit="/post/<>"
    )
    if request.method == "GET":
        return render_template("make-post.html", form=form, new=False)
    elif request.method == "POST":
        if form.validate_on_submit():
            post_to_update.title=form.title.data
            post_to_update.subtitle=form.subtitle.data
            post_to_update.img_url=form.img_url.data
            post_to_update.author=form.author.data
            post_to_update.body=form.body.data
            db.session.commit()
            posts = db.session.query(BlogPost).all()
            return redirect(url_for("show_post",index=post_to_update.id))

@app.route("/delete/<post_id>", methods=["GET", "POST"])
def delete(post_id):
    post_to_delete = BlogPost.query.get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    posts = db.session.query(BlogPost).all()
    return redirect(url_for("get_all_posts"))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)