import sqlalchemy
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import Column, Integer, String, Float, desc, asc
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, InputRequired
import requests
import sqlite3
from pprint import pprint

MOVIEDB_API_KEY = "598b3abafb89e98aabc3bcde425d6353"
MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
# db = sqlite3.connect("movies.db")
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
db = SQLAlchemy(app)


class Movie(db.Model):
    id = Column(Integer, unique=True)
    title = Column(String(250), unique=True, primary_key=True)
    year = Column(Integer, nullable=False)
    description = Column(String(250), nullable=False)
    rating = Column(Float)
    ranking = Column(Float)
    review = Column(String(250))
    img_url = Column(String(250))

# i = 1
# db.create_all()
# all_movies = db.session.query(Movie).all()
# for movie in all_movies:
#     print(movie.title)
#     movie.ranking = i
#     i += 1
# db.session.commit()

# all_movies = db.session.query(Movie).order_by(desc(Movie.rating)).all()
# all_movies = db.session.query(Movie).all()
# for movie in all_movies:
#     print(movie.title)
#     print(movie.ranking)

# exists = Movie.query.filter_by(title="Aladdin").first() is None
# print(exists)

# print(all_movies)
# for movie in all_movies:
#     print(movie.title)
#     print(movie.rating)
#     print(movie.id)

# possible_movie = Movie.query.filter_by()

# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# db.session.add(new_movie)
# db.session.commit()

class UpdateForm(FlaskForm):
    new_rating = StringField(label='Your Rating Out of 10 e.g. 7.5', validators=[InputRequired()])
    new_review = StringField(label='Your Review', validators=[InputRequired()])
    submit = SubmitField(label='Done')


class SearchForm(FlaskForm):
    new_movie_title = StringField(label='New Movie Title', validators=[InputRequired()])
    submit = SubmitField(label='Add Movie')


@app.route("/")
def home():
    all_movies = db.session.query(Movie).order_by(desc(Movie.rating)).all()
    i = 1
    for movie in all_movies:
        movie.ranking = i
        i += 1
    db.session.commit()
    all_movies = db.session.query(Movie).order_by(desc(Movie.ranking)).all()
    return render_template("index.html", movies=all_movies)


#
@app.route("/edit/<string:title>/<int:moviedbid>", methods=["GET", "POST"])
def edit(title, moviedbid):
    form = UpdateForm()
    if request.method == "GET":
        return render_template("edit.html", form=form, movie=Movie.query.get(title))
    elif request.method == "POST":
        if form.validate_on_submit():
            if Movie.query.filter_by(title=title).first() is not None:
                movie_to_edit = Movie.query.get(title)
                movie_to_edit.review = form.new_review.data
                # print(type(form.new_review.data))
                # print(type(form.new_rating.data))
                movie_to_edit.rating = form.new_rating.data
                db.session.commit()
                all_movies = db.session.query(Movie).all()
                return render_template("index.html", movies=all_movies)
            else:
                response = requests.get(
                    url=f"https://api.themoviedb.org/3/movie/{int(moviedbid)}?api_key={MOVIEDB_API_KEY}&language=en-US")
                img_file_path = response.json()["poster_path"]
                img_url = f"https://image.tmdb.org/t/p/w500/{img_file_path}"
                title = response.json()["title"]
                description = response.json()["overview"]
                year = response.json()["release_date"]
                pprint(response.json())
                pprint(response.json())
                new_movie = Movie(
                    title=f"{title}",
                    year=f"{year}",
                    description=f"{description}",
                    img_url=f"{img_url}",
                    review=form.new_review.data,
                    rating=form.new_rating.data
                )
                db.session.add(new_movie)
                db.session.commit()
                all_movies = db.session.query(Movie).all()
                return render_template("index.html", movies=all_movies)


@app.route("/delete/<string:value>", methods=["GET", "POST"])
def delete(value):
    # return render_template("index.html", movies=all_movies)
    movie_to_delete = Movie.query.get(value)
    if request.method == "GET":
        db.session.delete(movie_to_delete)
        db.session.commit()
        all_movies = db.session.query(Movie).all()
        return render_template("index.html", movies=all_movies)


@app.route("/add/", methods=["GET", "POST"])
def add():
    add_form = SearchForm()
    if request.method == "GET":
        return render_template("add.html", form=add_form, possible_movies=None)
    elif request.method == "POST":
        new_movie_name = add_form.new_movie_title.data
        response = requests.get(MOVIE_DB_SEARCH_URL, params={"api_key": MOVIEDB_API_KEY, "query": new_movie_name})
        possible_movies = response.json()["results"]
        print(possible_movies)
        # new_movie = Movie(title=f"{add_form.new_movie_title.data}")
        # db.session.add(new_movie)
        # db.session.commit()
        # all_movies = db.session.query(Movie).all()
        return render_template("add.html", form=add_form, possible_movies=possible_movies)


if __name__ == '__main__':
    app.run(debug=True)
