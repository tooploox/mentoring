import os
import shutil
import unittest

from http import HTTPStatus
from unittest import TestCase

from PIL import Image

from app import app
from tests.support import FlaskTestMixin


class TestRestApiBasics(TestCase, FlaskTestMixin):
    def setUp(self) -> None:
        self.test_client = app.test_client()
        os.makedirs(app.config['UPLOAD_FOLDER'])
        self.addCleanup(shutil.rmtree,
                        app.config['UPLOAD_FOLDER'],
                        ignore_errors=True)

    def test_upload_file(self):
        filename = 'mezoamerican_figures.jpg'
        source_path = os.path.join('data', filename)
        uploaded_file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        uploaded_scaled_file_path = os.path.join(app.config['UPLOAD_FOLDER'],
                                                 f'scaled_{filename}')
        with open(source_path, 'rb') as file:
            data = {
                'scale': '0.5',
                'files': [
                    (file, filename),
                ]
            }
            response = self.test_client.post(
                '/upload', data=data, follow_redirects=True,
                content_type='multipart/form-data'
            )

        self.assertEqual(HTTPStatus.OK, response.status_code)
        data = response.json[filename]
        self.assertEqual('0.5', data['data']['scale'])
        self.assertEqual('JPEG', data['data']['format'])
        self.assertEqual('RGB', data['data']['mode'])
        self.assertEqual([800, 376], data['data']['size'])
        uploaded_file_length = os.stat(uploaded_file_path).st_size
        original_file_length = os.stat(source_path).st_size
        self.assertEqual(original_file_length, uploaded_file_length)
        im = Image.open(uploaded_scaled_file_path)
        self.assertEqual((800, 376), im.size)

    def test_payload_too_large(self):
        filename = 'mayan_calendar.jpg'
        with open('data/mayan_calendar.jpg', 'rb') as file:
            data = {
                'scale': '0.5',
                'file': (file, filename)
            }
            response = self.test_client.post(
                '/upload', data=data, follow_redirects=True,
                content_type='multipart/form-data'
            )
        self.assertEqual(HTTPStatus.REQUEST_ENTITY_TOO_LARGE,
                         response.status_code)

    def test_get_upload(self):
        response = self.test_client.get('/upload')
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.json['message'])

    def test_client_status_ok(self):
        response = self.test_client.get('/')
        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertEqual('ok', response.json['status'])

    def test_page_not_found(self):
        response = self.test_client.get('/some_non_existing_page')
        self.assertEqual(HTTPStatus.NOT_FOUND, response.status_code)


if __name__ == '__main__':
    unittest.main()
