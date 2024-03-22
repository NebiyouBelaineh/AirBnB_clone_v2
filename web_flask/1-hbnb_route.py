#!/usr/bin/python3
"""script that starts a Flask web application:
    - listening on port 5000
    - '/' displays "Hello HBNB!"
    - '/hbnb' displays "HBNB"
    """
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def home():
    """Routes to '/'"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """Routes to '/hbnb'"""
    return "HBNB"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
