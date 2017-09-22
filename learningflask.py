from flask import Flask
import random

app = Flask(__name__)

@app.route("/hello")

def hello():
    return "Hello world!"

@app.route("/hellomyfriend")

def howyoudoin():
    return "How are you?"

@app.route("/quote")

def random_quote():
    quotes = ["You miss 100% of the shots you don't take.", "Reach for the moon. Even if you miss, you'll be among the stars.", "hahaha no inspirational quote for you :P try again!"]
    return quotes[int(random.random() * 3)]

if __name__ == '__main__':
    app.run(debug = True)