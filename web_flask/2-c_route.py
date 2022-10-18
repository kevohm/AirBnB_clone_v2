#!/usr/bin/python3
"""
A simple flask server running on 0.0.0.0:5000
"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def display_root():
    """Prints 'Hello HBNB!' to display"""
    return "Hello HBNB!"


@app.route('/hbnb')
def display_hbnb():
    """Prints 'HBNB' to display"""
    return "HBNB"

@app.route('/c/<text>')
def show_c_text(text):
    """prints c + text"""
    return f'c {escape(text)}'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
