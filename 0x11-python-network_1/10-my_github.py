#!/usr/bin/python3
"""Takes my Github creadentials and uses the GitHub API to displayy my id"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    r = requests.get('https://api.github.com/users/{}'.format(username),
            params={'token': password})
    json_data = r.json()
    print(json_data.get('id', None))
