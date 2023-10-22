#!/usr/bin/python3
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/c/<text>")
def test_path_variable(text):
    res = "C " + text
    return res.replace("_", " ")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
