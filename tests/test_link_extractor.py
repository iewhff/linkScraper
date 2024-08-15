import unittest
from consumer import LinkExtractor


class TestLinkExtractor(unittest.TestCase):
    def test_extract_links(self):
        html_content = """
        <html>
            <body>
                <a href="http://example.com/page1">Link 1</a>
                <a href="http://example.com/page2">Link 2</a>
            </body>
        </html>
        """
        # Initialize the LinkExtractor
        parser = LinkExtractor()

        # Feed the HTML content to the parser
        parser.feed(html_content)

        # Define the expected list of links
        expected_links = ["http://example.com/page1", "http://example.com/page2"]

        # Assert that the extracted links match the expected links
        self.assertEqual(parser.links, expected_links)


if __name__ == "__main__":
    unittest.main()
