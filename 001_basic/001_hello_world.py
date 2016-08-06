# coding: utf-8
"""
Flask hello world example

Run:

    python hello.py

Visit:

    http://localhost:5000

Or:

    export FLASK_APP=hello.py
    flask run
    # or
    python -m flask run

If you are on Windows you need to use set instead of export.

External Visibel Server:

    flask run --host=0.0.0.0

Debug Mode:

    export FLASK_DEEBUG=1
    flask run

"""

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()

