#!/usr/bin/python3
""" 3. Start a Flask web application with 4 views function"""
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/python")
@app.route("/python/<text>")
def test_path_variable_again(text="is cool"):
    res = "Python " + text
    return res.replace("_", " ")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
