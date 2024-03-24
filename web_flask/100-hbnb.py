#!/usr/bin/python3
"""Script that starts a Flask web application:
    - starts web application must be listening on 0.0.0.0, port 5000
    - uses storage for fetching data from the storage engine
    (FileStorage or DBStorage)
"""
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models import storage
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb')
def hbnb_filters():
    """displays HTML page with for Airbnb_clone"""
    data_state = storage.all(State).values()
    data_amenity = storage.all(Amenity).values()
    data_place = storage.all(Place).values()
    return render_template('100-hbnb.html', states=data_state, amenities=data_amenity)


@app.teardown_appcontext
def close_storage(exception):
    """Method to perform cleanup tasks to release resources associated
    with application context"""
    storage.close()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
