'''
Basic website based on FLASK (http://flask.pocoo.org)
'''

from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello World!"

@app.route('/about')
def about():
    return "About Page!"


if __name__ == '__main__':
    app.run(debug=True)
