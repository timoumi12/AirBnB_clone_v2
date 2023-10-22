#!/usr/bin/python3
""" a script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states")
def cities_by_states():
    states = storage.all("State")
    return render_template("9-states.html",
                           states=states)


@app.route("/states/<id>")
def cities_by_states(id):
    states = storage.all("State")
    for state in states:
        if state.id == id:
            render_template("9-states.html",
                            state=state)
    render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
