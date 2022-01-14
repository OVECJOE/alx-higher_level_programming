#!/usr/bin/python3
"""Sends a POST request to the passed URL with the email as a parameter
and finally displays the body of the response"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    payload = {'email': sys.argv[2]}
    r = requests.post(url, data=payload)
    print(r.text)
