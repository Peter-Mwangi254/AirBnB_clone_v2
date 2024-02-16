#!/usr/bin/python3
"""Starts a Flask web application
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ” followed by the value of the text variable
    (replace underscore _ symbols with a space )
    /python/<text>: display “Python ”, followed by the value of
    the text variable (replace underscore _ symbols with a space )
        The default value of text is “is cool”
    /number/<n>: display “n is a number” only if n is an integer
    /number_template/<n>: display a HTML page only if n is an integer:
        H1 tag: “Number: n” inside the tag BODY
    /number_odd_or_even/<n>: display a HTML page only if n is an integer:
        H1 tag: “Number: n is even|odd” inside the tag BODY
"""

from flask import Flask, render_template
from markupsafe import escape


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


@app.route("/c/<text>")
def c_text(text):
    """Displays “C ” followed by the value of the text variable
    """
    modified_text = text.replace("_", " ")
    return f"C {escape(modified_text)}"


@app.route("/python/", defaults={'text': 'is_cool'})
@app.route("/python/<text>")
def python_text(text="is cool"):
    """Displays “Python ”, followed by the value of the text variable
    """
    modified_text = text.replace("_", " ")
    return f"Python {escape(modified_text)}"


@app.route("/number/<int:n>")
def number(n):
    """Display “n is a number” only if n is an integer
    """
    return f"{escape(n)} is a number"


@app.route("/number_template/<int:n>")
def number_temp(n):
    """Display a HTML page only if n is an integer
    """
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>")
def odd_or_even(n):
    """Display a HTML page only if n is an integer
    """
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
