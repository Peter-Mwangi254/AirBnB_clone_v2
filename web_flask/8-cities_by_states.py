#!/usr/bin/python3
"""Starts a Flask web application
Routes:
    /cities_by_states: display a HTML page: (inside the tag BODY)
        H1 tag: “States”
        UL tag: with the list of all State objects present in DBStorage
        sorted by name (A->Z) tip
        LI tag: description of one State: <state.id>: <B><state.name></B>
          + UL tag: with the list of City objects linked to the State
            sorted by name (A->Z)
                LI tag: description of one City: <city.id>: <B><city.name></B>
"""

from flask import Flask, render_template
from models import storage
from models.state import State, City

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/cities_by_states")
def cities_by_states():
    """Display a HTML page
    """
    return render_template("8-cities_by_states.html",
                           cities=storage.all(City),
                           states=storage.all(State))


@app.route("/states_list")
def teardown_appcontext():
    """Remove the current SQLAlchemy Session after each session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
