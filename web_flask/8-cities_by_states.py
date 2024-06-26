#!/usr/bin/python3
"""Script that starts a Flask web application:
    - starts web application must be listening on 0.0.0.0, port 5000
    - uses storage for fetching data from the storage engine
    (FileStorage or DBStorage)
"""
from models.state import State
from models import storage
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_storage(exception=None):
    """Method to perform cleanup tasks to release resources associated
    with application context"""
    storage.close()


@app.route('/cities_by_states')
def city_by_states():
    """displays HTML page with cities by state"""
    all_states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=all_states)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
