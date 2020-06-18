import unittest

from unittest import TestCase
from tests.support import FlaskTestMixin
from app import app


class TestFlask102BmiAsUrl(TestCase, FlaskTestMixin):
    def setUp(self):
        self.test_client = app.test_client()

    def format_bmi_params(self, **kwargs):
        params = '&'.join([f'{key}={value}' for key, value in kwargs.items()])
        return f'?{params}'

    def test_bmi_ok(self):
        params = self.format_bmi_params(height=1.75, weight=78.5)
        response = self.test_client.get(f'/bmi/{params}')
        self.assertEqual(200, response.status_code)
        self.assertEqual(25.63, response.json['bmi'])

    def test_bmi__missing_height(self):
        params = self.format_bmi_params(weight=78.5)
        response = self.test_client.get(f'/bmi/{params}')
        self.assertEqual(400, response.status_code)
        self.assertEqual(b"Missing 'height' parameter", response.data)

    def test_bmi__bad_height_format(self):
        params = self.format_bmi_params(height='height', weight=78.5)
        response = self.test_client.get(f'/bmi/{params}')
        self.assertEqual(400, response.status_code)
        self.assertEqual(b"could not convert string to float: 'height'",
                         response.data)

    def test_bmi__missing_weight(self):
        params = self.format_bmi_params(height=1.75)
        response = self.test_client.get(f'/bmi/{params}')
        self.assertEqual(400, response.status_code)
        self.assertEqual(b"Missing 'weight' parameter", response.data)

    def test_bmi__bad_weight_format(self):
        params = self.format_bmi_params(height=1.75, weight='heavy')
        response = self.test_client.get(f'/bmi/{params}')
        self.assertEqual(400, response.status_code)
        self.assertEqual(b"could not convert string to float: 'heavy'",
                         response.data)

    def test_bmi__too_tall(self):
        params = self.format_bmi_params(height=5.53, weight=100.0)
        response = self.test_client.get(f'/bmi/{params}')
        self.assertEqual(400, response.status_code)
        self.assertEqual(b'Height should be in range (0.0, 3.0>', response.data)

    def test_bmi__too_short(self):
        params = self.format_bmi_params(height=0, weight=80.0)
        response = self.test_client.get(f'/bmi/{params}')
        self.assertEqual(400, response.status_code)
        self.assertEqual(b'Height should be in range (0.0, 3.0>', response.data)

    def test_bmi__too_heavy(self):
        params = self.format_bmi_params(height=1.53, weight=1024.0)
        response = self.test_client.get(f'/bmi/{params}')
        self.assertEqual(400, response.status_code)
        self.assertEqual(b'Weight should be in range (0.0, 1000.0>',
                         response.data)

    def test_bmi__too_light(self):
        params = self.format_bmi_params(height=1.63, weight=-10.5)
        response = self.test_client.get(f'/bmi/{params}')
        self.assertEqual(400, response.status_code)
        self.assertEqual(b'Weight should be in range (0.0, 1000.0>',
                         response.data)


class TestFlask102BmiAsPathParameters(TestCase, FlaskTestMixin):
    def setUp(self):
        self.test_client = app.test_client()

    def format_bmi_params(self, height='', weight=''):
        return f'height/{height}/weight/{weight}/'

    def test_bmi_ok(self):
        params = self.format_bmi_params(height=1.75, weight=78.5)
        response = self.test_client.get(f'/bmi2/{params}')
        self.assertEqual(200, response.status_code)
        self.assertEqual(25.63, response.json['bmi'])

    def test_bmi__missing_height(self):
        params = self.format_bmi_params(weight=78.5)
        response = self.test_client.get(f'/bmi2/{params}')
        self.assertEqual(404, response.status_code)

    def test_bmi__bad_height_format(self):
        params = self.format_bmi_params(height='height', weight=78.5)
        response = self.test_client.get(f'/bmi2/{params}')
        self.assertEqual(404, response.status_code)

    def test_bmi__missing_weight(self):
        params = self.format_bmi_params(height=1.75)
        response = self.test_client.get(f'/bmi2/{params}')
        self.assertEqual(404, response.status_code)

    def test_bmi__bad_weight_format(self):
        params = self.format_bmi_params(height=1.75, weight='heavy')
        response = self.test_client.get(f'/bmi2/{params}')
        self.assertEqual(404, response.status_code)

    def test_bmi__too_tall(self):
        params = self.format_bmi_params(height=5.53, weight=100.0)
        response = self.test_client.get(f'/bmi2/{params}')
        self.assertEqual(400, response.status_code)
        self.assertEqual(b'Height should be in range (0.0, 3.0>', response.data)

    def test_bmi__too_short(self):
        params = self.format_bmi_params(height=0.0, weight=80.0)
        response = self.test_client.get(f'/bmi2/{params}')
        self.assertEqual(400, response.status_code)
        self.assertEqual(b'Height should be in range (0.0, 3.0>', response.data)

    def test_bmi__too_heavy(self):
        params = self.format_bmi_params(height=1.53, weight=1024.0)
        response = self.test_client.get(f'/bmi2/{params}')
        self.assertEqual(400, response.status_code)
        self.assertEqual(b'Weight should be in range (0.0, 1000.0>',
                         response.data)

    def test_bmi__too_light(self):
        params = self.format_bmi_params(height=1.63, weight=-10.5)
        response = self.test_client.get(f'/bmi2/{params}')
        self.assertEqual(400, response.status_code)
        self.assertEqual(b'Weight should be in range (0.0, 1000.0>',
                         response.data)


if __name__ == '__main__':
    unittest.main()

