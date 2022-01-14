#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status"""
import urllib.request


if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        page = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(page)))
        print("\t- content: {}".format(page))
        print("\t- utf8 content: {}".format(page.decode("utf-8")))
