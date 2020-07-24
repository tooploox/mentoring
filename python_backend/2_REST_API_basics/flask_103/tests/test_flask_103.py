import json
import unittest

from unittest import TestCase
from tests.support import FlaskTestMixin
from app import app


class TestRestApiBasics(TestCase, FlaskTestMixin):
    def setUp(self) -> None:
        self.test_client = app.test_client()

    def test_upload_file(self):
        data = {'action': 'scale',
                'value': '0.5',
                'file': (open('data/dog-image.jpg', 'rb'), 'dog-image.jpg')}

        response = self.test_client.post(
            '/upload', data=data, follow_redirects=True,
            content_type='multipart/form-data'
        )
        self.assertEqual(200, response.status_code)
        data = response.json
        self.assertEqual('scale', data['data']['action'])
        self.assertEqual('0.5', data['data']['value'])

    def test_client_status_ok(self):
        response = self.test_client.get('/')
        self.assertEqual(200, response.status_code)
        self.assertEqual('ok', response.json['status'])

    def test_page_not_found(self):
        response = self.test_client.get('/some_non_existing_page')
        self.assertEqual(404, response.status_code)


if __name__ == '__main__':
    unittest.main()
