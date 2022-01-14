#!/usr/bin/python3
"""Sends a search parameter to a URL."""
import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    search_query = sys.argv[1] if len(sys.argv) > 1 else ""
    data = {'q': search_query}
    r = requests.post(url, data=data)
    try:
        content = r.json()
        if content:
            print("[{}] {}".format(content['id'], content['name']))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
