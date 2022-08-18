from flask import Flask, render_template, request, flash, redirect, render_template, session, url_for
#from jinja2.utils import markupsafe
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField, PasswordField, EmailField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, Email
from markupsafe import Markup
from flask_bootstrap import Bootstrap

SECRET_KEY = "secret"
EMAIL = "admin@email.com"
PASSWORD = "12345678"

app = Flask(__name__)
app.config.from_object(__name__)
Bootstrap(app)

@app.route("/")
def home():
    return render_template('index.html')

class LoginForm(FlaskForm):
    email = EmailField(label="Email", validators=[DataRequired(), Email(message="Invalid Email Address.")])
    password = PasswordField(label="Password", validators=[DataRequired(), Length(min=8, message="Field must be at "
                                                                                                 "least 8 characters "
                                                                                                 "long.")])
    submit = SubmitField(label="Login")
    #recaptcha = RecaptchaField()

@app.route("/login", methods=["GET", "Post"])
def login():
    form = LoginForm()
    if request.method == "GET":
        return render_template("login.html", form=form)
    else:
        print("POST REQUEST")
        if form.validate_on_submit():
            print(form.email.data == EMAIL and form.password.data == PASSWORD)
            if form.email.data == EMAIL and form.password.data == PASSWORD:
                return render_template('success.html')
            else:
                return render_template('denied.html')
        else:
            return render_template("login.html", form=form)



if __name__ == '__main__':
    app.run(debug=True)