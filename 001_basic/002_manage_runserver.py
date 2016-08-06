# coding: utf-8
"""
Flask manager script example

Run like Django:

    python manage.py runserver
    python manage.py shell

"""

from flask import Flask
from flask.ext.script import Manager
app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

if __name__ == '__main__':
    manager.run()
