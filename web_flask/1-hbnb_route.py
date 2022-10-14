#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
        return "Hello HBNB!"
@app.route("/hbnb")
def hello():
    return "HBNB"
if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
