import unittest

from unittest import TestCase
from tests.support import FlaskTestMixin
from app import app


class TestRestApiBasics(TestCase, FlaskTestMixin):
    def setUp(self) -> None:
        self.test_client = app.test_client()

    def test_client_status_ok(self):
        response = self.test_client.get('/')
        self.assertEqual(200, response.status_code)
        self.assertEqual('ok', response.json['status'])

    def test_page_not_found(self):
        response = self.test_client.get('/some_non_existing_page')
        self.assertEqual(404, response.status_code)


if __name__ == '__main__':
    unittest.main()
