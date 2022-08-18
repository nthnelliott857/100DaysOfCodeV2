from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Table, MetaData

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books.db"
db = SQLAlchemy(app)


class Book(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(250), unique=True, nullable=False)
    author = Column(String(250), nullable=False)
    rating = Column(Float, nullable=False)

all_books = db.session.query(Book).all()


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html", library=all_books)
    elif request.method == "POST":
        return render_template("index.html")


@app.route('/delete/<string:value>', methods=["GET", "POST"])
def delete(value):
    if request.method == "GET":
        book_to_delete = Book.query.get(value)
        db.session.delete(book_to_delete)
        db.session.commit()
        all_books = db.session.query(Book).all()
        return render_template("index.html", library=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        print(request.form)
        new_book = Book(title= request.form["title"], author=request.form["author"], rating=request.form["rating"])
        db.session.add(new_book)
        db.session.commit()
        all_books = db.session.query(Book).all()
        return render_template("index.html", library=all_books)
    return render_template("add.html")


@app.route("/edit/<string:value>", methods=["GET", "POST"])
def edit(value):
    book_to_edit = Book.query.get(value)
    if request.method == "GET":
        return render_template("edit.html", title=book_to_edit.title, rating=book_to_edit.rating, id=value)
    elif request.method == "POST":
        book_to_edit.rating = request.form["rating"]
        db.session.commit()
        all_books = db.session.query(Book).all()
        return render_template("index.html", library=all_books)

if __name__ == "__main__":
    app.run(debug=True)
