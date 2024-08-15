import re
from html.parser import HTMLParser


class LinkExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for attr in attrs:
                if attr[0] == "href":
                    self.links.append(attr[1])


def consumer(q, output_file):
    # Dictionary to store links by URL
    links_by_url = {}

    while True:
        item = q.get()
        if item is None:
            # Signal that production has finished
            break

        url, html_content = item

        # Initialize the parser and feed it with the HTML content
        parser = LinkExtractor()
        parser.feed(html_content)

        # Store all the links found in the parser.links list
        links_by_url[url] = parser.links

        q.task_done()

    # After processing all items, save the links to a file
    with open(output_file, "w") as f:
        for url, links in links_by_url.items():
            f.write(f"Links extracted from {url}:\n")
            for link in links:
                f.write(f"{link}\n")
            f.write("\n")  # Blank line between different URLs
