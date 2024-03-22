#!/usr/bin/python3
"""script that starts a Flask web application:
    - listening on port 5000
    - '/' displays "Hello HBNB!"
    - '/hbnb' displays "HBNB"
    - /c/<text>: display “C ” followed by the value of the text variable
    (replace underscore _ symbols with a space )
    - /python/<text>: display “Python ”, followed by the value of the text
    variable (replace underscore _ symbols with a space )
      - The default value of text is “is cool”
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


@app.route('/c/<path:text>')
def c_text(text):
    """Routes to 'c' and obtains path after it"""
    text = text.replace('_', ' ')
    return f'C {text}'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
