from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def login_page():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def receive_data():
    if request.method == 'POST':
        credentials = {"username": request.form["name"],
                       "password": request.form["password"]}
        # print(credentials)
        # return("hello, world")
        #print(credentials)
        return render_template("in.html", credentials=credentials)


if __name__ == "__main__":
    app.run(debug=True)
