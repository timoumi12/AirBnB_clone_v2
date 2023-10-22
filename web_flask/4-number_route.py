#!/usr/bin/python3
""" 4. Start a Flask web application with 5 views function"""
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/number/<int:n>")
def test_path_variable_integer(n):
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)