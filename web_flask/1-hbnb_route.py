#!/usr/bin/python3
"""Starts a Flask web application
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_hbnb():
    """Starts a Flask web application
    """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """Displays HBNB
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
