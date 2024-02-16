#!/usr/bin/python3
"""Starts a Flask web application
Routes:
    /states_list: display a HTML page: (inside the tag BODY)
        H1 tag: “States”
        UL tag: with the list of all State objects present in DBStorage
        sorted by name (A->Z) tip
        LI tag: description of one State: <state.id>: <B><state.name></B>!”
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states_list")
def states_list():
    """Display a HTML page
    """
    return render_template("7-states_list.html",
                           state_storage=storage.all(State))


@app.route("/states_list")
def teardown_appcontext():
    """Remove the current SQLAlchemy Session after each session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
