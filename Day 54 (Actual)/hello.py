from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello!</p>"

def make_bold(function):
    def wrapper_function():
        output = function()
        return f'<b>{output}</b>'
    return wrapper_function

def make_emphasis(function):
    def wrapper_function():
        output = function()
        return f'<em>{output}</em>'
    return wrapper_function

def make_underlined(function):
    def wrapper_function():
        output = function()
        return f'<u>{output}</u>'
    return wrapper_function



@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye"

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hi, {name}, you are {number} years old!"

if __name__ == "__main__":
    app.run(debug=True)

