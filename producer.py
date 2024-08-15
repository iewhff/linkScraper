import urllib.request
import importlib.util


# Verify if `chardet` is available
def is_chardet_available():
    return importlib.util.find_spec("chardet") is not None


# Try decoding with UTF-8, and if it fails, use `chardet` if available
def fetch_html(url):
    try:
        # Open the URL and read the content
        with urllib.request.urlopen(url) as response:
            raw_data = response.read()

            # Try decoding with UTF-8
            try:
                html = raw_data.decode("utf-8")
            except UnicodeDecodeError:
                # If UTF-8 decoding fails, use `chardet` if available
                if is_chardet_available():
                    # I dont know if this is allowed, but it works
                    import chardet

                    detected_encoding = chardet.detect(raw_data)["encoding"]
                    html = raw_data.decode(detected_encoding)
                else:
                    # If `chardet` is not available, decode with fallback encoding
                    html = raw_data.decode("latin1")  # or another fallback encoding

        return html
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None
