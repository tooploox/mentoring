"""Flask tutorial 103

Write your code below.
Details in the readme.md file.
"""

import os

from flask import Flask, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'upload'
app.config['MAX_CONTENT_PATH'] = 512_000  # 500 kB

@app.route('/')
def index():
    return {'status': 'ok'}


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # return str(request.files)
        f = request.files['file']
        path = os.path.join(app.config['UPLOAD_FOLDER'],
                            secure_filename(f.filename))
        f.save(path)
        data = request.values
        return f'file {f.filename} uploaded successfully, data {data!r}'
    else:
        return "POST your files here"


if __name__ == '__main__':
    app.run(debug=True)
