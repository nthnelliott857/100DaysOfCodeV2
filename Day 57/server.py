from flask import Flask, render_template
import datetime
import requests
import json

app = Flask(__name__)
CURRENT_DATE = datetime.datetime.now().year
MY_NAME = "Nathaniel Elliott"

@app.route("/")
def hello_world():
    return render_template("index.html", copyright=f"Copyright {CURRENT_DATE}. Built by {MY_NAME}.")

@app.route("/guess/<string:name>")
def guess(name):
    age_result = requests.get(url=f"https://api.agify.io?name={name}").json()
    age = age_result["age"]
    gender_result = requests.get(url=f"https://api.genderize.io?name={name}").json()
    gender = gender_result["gender"]
    return render_template("guess.html", name=name, age=age, gender=gender)
#return f"{name}"

@app.route("/blog")
def blog():
    blog_response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = blog_response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)
