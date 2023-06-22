import random
from flask import Flask

random_number = random.randint(0, 9)
print(f"Random number: {random_number}")

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper


def user_won():
    return f'<h1 style="color: green">You found me!</h1>' \
           '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width=500>'


def user_low():
    return f'<h1 style="color: red">Too low, try again!</h1>' \
           '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width=500>'


def user_high():
    return f'<h1 style="color: blue">Too high, try again!</h1>' \
           '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width=500>'


@app.route('/')
def hello_world():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<p>Ex. 127.X.X.X:XXXX/7</p>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=500>'


@app.route('/<int:number>')
def user_guess(number):
    if number == random_number:
        return user_won()
    elif number < random_number:
        return user_low()
    elif number > random_number:
        return user_high()


if __name__ == '__main__':
    app.run(debug=True)
