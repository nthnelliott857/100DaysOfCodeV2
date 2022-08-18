from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    blog_response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = blog_response.json()
    return render_template("index.html", posts=all_posts)

@app.route("/blog/<int:num>")
def get_blog(num):
    blog_response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = blog_response.json()
    post = all_posts[num - 1]
    return render_template("post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)
