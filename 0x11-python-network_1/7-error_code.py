#!/usr/bin/python3
"""Sends a request to the URL, and displays the body of the response"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    if not r.ok:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
