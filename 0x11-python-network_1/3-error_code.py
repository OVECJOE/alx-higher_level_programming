#!/usr/bin/python3
"""Sends a request to the URL and displays the body of the response"""
from urllib.request import urlopen
from urllib.parse import urlparse
from urllib.error import HTTPError
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urlopen(url) as response:
            page = response.read()
            print(page.decode('utf-8'))
    except HTTPError as e:
        print('Error code: {}'.format(e.code))
