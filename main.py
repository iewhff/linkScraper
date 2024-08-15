import threading
import queue
from producer import fetch_html
from consumer import consumer

# List of URLs to process
urls = ["http://google.com", "http://yahoo.com", "https://github.com/"]

# Output file name
output_file = "extracted_links.txt"

# Create a queue to store the HTML content
q = queue.Queue()


def producer_worker(url, q):
    html_content = fetch_html(url)
    if html_content:
        q.put((url, html_content))


# Create multiple threads to run the producer concurrently
producer_threads = []
for url in urls:
    thread = threading.Thread(target=producer_worker, args=(url, q))
    producer_threads.append(thread)
    thread.start()

# Start the consumer thread
consumer_thread = threading.Thread(target=consumer, args=(q, output_file))
consumer_thread.start()

# Wait for all producer threads to finish
for thread in producer_threads:
    thread.join()

# Put None in the queue to signal the consumer that production has finished
q.put(None)

# Wait for the consumer thread to finish
consumer_thread.join()
