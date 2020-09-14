"""Flask tutorial 103

Write your code below.
Details in the readme.md file.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return {'status': 'ok'}


if __name__ == '__main__':
    app.run(debug=True)
