#!/usr/bin/python3
"""
Simple flask application listening on 0.0.0.0 port 5000
"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def hello_hbnb():
	"Returns Hello BNB!"
	return "Hello HBNB!"

@app.route('/hbnb')
def hbnb():
	"Route returns HBNB"
	return "HBNB"

@app.route('/c/<text>')
def c_text(text):
	"Returns C followed by value of text"
	return 'C {}'.format(text.replace('_', ' '))

@app.route("/python/", defaults={"text": "is_cool"})
@app.route('/python/<text>')
def python(text):
	"Returns Python followed by some text"
	return 'Python {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
	app.run(host="0.0.0.0")
