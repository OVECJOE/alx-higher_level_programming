#!/usr/bin/python3
"""Displays the value of the variable X-Request-Id in the response header"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    request_id = r.headers.get('X-Request-Id', None)
    print(request_id)
