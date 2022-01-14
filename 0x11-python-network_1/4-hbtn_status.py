#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status using requests"""
import requests

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    resp = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(resp.text)))
    print("\t- content: {}".format(resp.text))
