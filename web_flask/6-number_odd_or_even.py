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
    - /python/: displays 'Python is cool'
    - /number/<n>: display “n is a number” only if n is an integer
    - /number_template/<n>: display a HTML page only if n is an integer:
      - H1 tag: “Number: n” inside the tag BODY
    """
from flask import Flask, render_template


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


@app.route('/python/<text>')
def python_text(text):
    """Routes to 'python' and obtains path after it"""
    text = text.replace('_', ' ')
    return f'Python {text}'


@app.route('/python')
def python_default(text='is cool'):
    """Routes to 'python'"""
    return f'Python is cool'


@app.route('/number/<int:n>')
def number(n):
    """Routes to 'number' and obtains path after it"""
    return f'{n} is a number'


@app.route('/number_template/<int:n>')
def number_template(n):
    """Routes to number template if n is an integer"""
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """Routes to number odd or even template if n is an integer"""
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
