#!/usr/bin/python3
"""Starts a Flask web application
Routes:
    /hbnb_filters: display a HTML page
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/hbnb_filters")
def states():
    """Displays a HTML page
    """
    state_objs = list(storage.all(State).values())
    amenity_objs = list(storage.all(Amenity).values())
    return render_template('10-hbnb_filters.html',
                           state_objs=state_objs, amenity_objs=amenity_objs)


@app.teardown_appcontext
def teardown(self):
    """Remove the current SQLAlchemy Session after each session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
