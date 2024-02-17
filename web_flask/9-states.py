#!/usr/bin/python3
"""Starts a Flask web application
Routes:
    /states: display a HTML page: (inside the tag BODY)
        H1 tag: “States”
        UL tag: with the list of all State objects present in DBStorage
        sorted by name (A->Z) tip
        LI tag: description of one State: <state.id>: <B><state.name></B>
    /states/<id>: display a HTML page: (inside the tag BODY)
        If a State object is found with this id:
        H1 tag: “State: ”
        H3 tag: “Cities:”
        UL tag: with the list of City objects linked to the State sorted
        by name (A->Z)
        LI tag: description of one City: <city.id>: <B><city.name></B>
        Otherwise:
        H1 tag: “Not found!”
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states")
def states():
    """Displays a HTML page
    """
    return render_template("9-states.html",
                           state=storage.all(State))


@app.route("/states/<id>")
def states_id(id):
    """Display a HTML page
    """
    for state in storage.all(State).values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(self):
    """Remove the current SQLAlchemy Session after each session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
