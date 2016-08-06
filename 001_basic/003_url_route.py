# coding: utf-8
"""
Flask url param example
"""

from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/agent')
def agent():
    ua = request.headers.get('User-Agent')
    return '<h1>Hello %s!</h1>' % ua

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name

@app.route('/post/<int:post_id>')
def show_post(post_id):
    """
    show the post with the given id, the id is an integer
    The following converters exist:
    - string: text without slash (default)
    - int
    - float
    - path: like string but accept slash
    - any: matches one of the items, similar to choices
    - uuid
    """
    return 'Post %d' % post_id

if __name__ == '__main__':
    print app.url_map
    app.run(debug=True)
