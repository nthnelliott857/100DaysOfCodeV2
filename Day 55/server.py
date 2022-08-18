from flask import Flask
import random
import html

app = Flask(__name__)
RANDOM_NUMBER = random.randint(0, 9)

@app.route("/")
def hello_world():
    return '<h1>Guess a number between 0 and 9: </h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


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

#@make_bold


def stylize_text(function):
    def wrapper(*args, **kwargs):
        output = function(*args, **kwargs)
        output = f"<b>{output}</b>"
        return output
    return wrapper


@app.route("/<int:number>")
@stylize_text
def user_guesses(number):
    print(number)
    print(RANDOM_NUMBER)
    if RANDOM_NUMBER > number:
        return "<h1 style='color: red'>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    elif number > RANDOM_NUMBER:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)