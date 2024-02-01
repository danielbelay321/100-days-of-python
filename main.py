from flask import Flask
from markupsafe import escape
from random import choice, randint



app = Flask(__name__)

random_number = randint(0,9)

@app.route('/<int:number>')
def hello(number):

    if number < random_number:
        return "<h1 style='color:red;'>Too Low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' alt='number guess'>"
    elif number > random_number:
        return "<h1 style='color:red;'>Too High, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' alt='number guess'>"
    else:
        return "<h1 style='color:green;'>Congratulation!, Yo got it!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' alt='number guess'>"







if __name__ == "__main__":
    app.run(debug=True)


