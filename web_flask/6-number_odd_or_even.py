#!/usr/bin/python3
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/number_odd_or_even/<int:n>")
def test_path_variable_if(n):
    if n % 2 == 0:
        return render_template("6-number_odd_or_even.html", number=n,
                               state="even")
    else:
        return render_template("6-number_odd_or_even.html", number=n,
                               state="odd")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
