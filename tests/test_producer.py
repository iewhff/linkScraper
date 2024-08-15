import unittest
from unittest.mock import patch, MagicMock
from producer import fetch_html


class TestFetchHtml(unittest.TestCase):
    @patch("urllib.request.urlopen")
    def test_fetch_html_success(self, mock_urlopen):
        # Simulate a successful urlopen response
        mock_response = MagicMock()
        mock_response.read.return_value = b"<html><body>Hello World</body></html>"
        mock_urlopen.return_value = mock_response

        url = "http://example.com"
        html = fetch_html(url)
        self.assertEqual(html, "<html><body>Hello World</body></html>")

    @patch("urllib.request.urlopen")
    def test_fetch_html_failure(self, mock_urlopen):
        # Simulate an exception from urlopen
        mock_urlopen.side_effect = Exception("Error fetching URL")

        url = "http://example.com"
        html = fetch_html(url)
        self.assertIsNone(html)


if __name__ == "__main__":
    unittest.main()
