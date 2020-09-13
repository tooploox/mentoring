"""Flask tutorial 103

Write your code below.
Details in the readme.md file.
"""

import os

from flask import Flask, request
from PIL import Image
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'upload'
app.config['MAX_CONTENT_LENGTH'] = 450_000


def get_secure_filename(filename):
    return os.path.join(app.config['UPLOAD_FOLDER'],
                        secure_filename(filename))


@app.route('/')
def index():
    return {'status': 'ok'}


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        files = request.files.getlist('files')
        response = {}
        for file in files:
            path = get_secure_filename(file.filename)
            file.save(path)
            data = {}
            im = Image.open(path)
            data['mode'] = im.mode
            data['format'] = im.format
            scale = float(request.values.get('scale'))
            if scale:
                im = im.resize(
                    (int(im.size[0] * scale), int(im.size[1] * scale)),
                    Image.ANTIALIAS)
                resized_file_path = get_secure_filename(
                    f'scaled_{file.filename}')
                im.save(resized_file_path)
                data['scale'] = scale
                data['size'] = im.size

            message = f'file {file.filename!r} uploaded successfully.'
            response[file.filename] = dict(message=message, data=data)
        return response
    else:
        return {'message': 'POST your files here'}


if __name__ == '__main__':
    app.run(debug=True)
