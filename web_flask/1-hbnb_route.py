#!/usr/bin/python3
""" 1. Start a Flask web application with 2 views function"""
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/hbnb")
def test_hbnb():
    """returns hbnb"""
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
