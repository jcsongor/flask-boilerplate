from unittest import TestCase

from app import app

class HttpTestCase(TestCase):
    def setUp(self):
        app.testing = True
        self._client = app.test_client()

    def _get(self, url):
        self._client.get(url)

    def _get_response_data(self, url):
        return self._client.get(url).data.decode('utf-8')

    def _get_response_status(self, url):
        return self._client.get(url).status_code


class TestPageNotFound(HttpTestCase):
    def test_nonexistent_urls_respond_with_404(self):
        self.assertEqual(self._get_response_status('/nonexistent_url'), 404)

    def test_nonexistent_urls_respond_with_correct_message(self):
        self.assertIn('The requested URL was not found on the server', self._get_response_data('/nonexistent_url'))


class TestHealthCheck(HttpTestCase):
    def test_healthcheck_responds_with_200(self):
        self.assertEqual(self._get_response_status('/healthcheck'), 200)

    def test_healthcheck_responds_with_ok(self):
        self.assertEqual(self._get_response_data('/healthcheck'), 'OK')

