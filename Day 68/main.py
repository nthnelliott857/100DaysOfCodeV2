import flask
import werkzeug.security
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'InTheJungleTheMightyJungleTheLionSleepsTonight'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


# Line below only required once, when creating DB.
# db.create_all()
users = db.session.query(User).all()
# for user in users:
#     print(user.email)


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        if User.query.filter_by(email=request.form["email"]).first() is None:
            new_user_account = User(
                name=request.form["name"],
                email=request.form["email"],
                password=werkzeug.security.generate_password_hash(password=request.form["password"], method='pbkdf2:sha256', salt_length=8)
            )
            db.session.add(new_user_account)
            db.session.commit()
            login_user(new_user_account)
            return redirect(url_for('secrets'))
        else:
            flash("You've already signed up with that email, log in instead!", 'error')
            return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        users = db.session.query(User).all()
        email = request.form["email"]
        user = User.query.filter_by(email=email).first()
        if user is not None:
            if check_password_hash(pwhash=user.password, password=request.form["password"]):
                login_user(user)
                return redirect(url_for("secrets"))
            else:
                flash("Password Incorrect, please try again.", 'error')
                return render_template("login.html")
        else:
            flash('Email does not exist, please try again.', 'error')
            return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    # flash(f'{current_user.name} just logged in.')
    return render_template("secrets.html", name=current_user.name, logged_in=current_user.is_authenticated)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory(
        directory="static", path='files/cheat_sheet.pdf', as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)
