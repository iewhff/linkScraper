import unittest
import queue
from consumer import consumer, LinkExtractor
from unittest.mock import patch


class TestConsumer(unittest.TestCase):
    @patch("builtins.print")
    def test_consumer_extracts_links(self, mock_print):
        q = queue.Queue()

        # Add an item to the queue for processing
        url = "http://example.com"
        html_content = """
        <html>
            <body>
                <a href="http://example.com/page1">Link 1</a>
                <a href="http://example.com/page2">Link 2</a>
            </body>
        </html>
        """
        q.put((url, html_content))

        # Add None to signal the end of processing
        q.put(None)

        # Run the consumer
        consumer(q, "dummy_output_file.txt")  # Filename is not used in this test

        # Verify that the links were printed
        mock_print.assert_any_call(f"Links extracted from {url}:")
        mock_print.assert_any_call("http://example.com/page1")
        mock_print.assert_any_call("http://example.com/page2")


if __name__ == "__main__":
    unittest.main()
