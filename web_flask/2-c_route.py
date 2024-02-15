#!/usr/bin/python3
"""Starts a Flask web application
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ” followed by the value of the text variable
    (replace underscore _ symbols with a space )
"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Starts a Flask web application
    """
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays HBNB
    """
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """Displays “C ” followed by the value of the text variable
    """
    modified_text = text.replace("_", " ")
    return f"C {escape(modified_text)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
