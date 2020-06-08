"""Flask tutorial 101 - solution

Details in the readme.md file.
"""


from flask import Flask

app = Flask(__name__)


@app.route("/")
def status():
    return dict(status="ok")


if __name__ == '__main__':
    app.run()
