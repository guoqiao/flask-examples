# coding: utf-8
"""
Flask static file example

create a dir `static`, and use `url_for`
Should used in debug mode only.
"""
from flask import Flask, url_for
app = Flask(__name__)

@app.route("/")
def hello():
    url = url_for('static', filename='style.css')
    return "url for static: {}".format(url)

if __name__ == "__main__":
    app.run()

