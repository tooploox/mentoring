"""Base test class for flask apps.

It can be used to test basic flask app functionality.
"""


class FlaskTestMixin:
    def test_client_status_ok(self):
        response = self.test_client.get('/')
        self.assertEqual(200, response.status_code)
        self.assertEqual('ok', response.json['status'])

    def test_page_not_found(self):
        response = self.test_client.get('/some_non_existing_page')
        self.assertEqual(404, response.status_code)
