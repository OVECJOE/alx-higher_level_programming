#!/usr/bin/python3
"""Takes a URL, sends a request to the URL, and displays the
value of the X-Request-Id variable found in the header"""
from urllib.request import urlopen
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urlopen(url) as response:
        print(response.headers.get('X-Request-Id', None))
