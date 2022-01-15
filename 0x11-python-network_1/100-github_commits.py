#!/usr/bin/python3
"""Retrieves the last 10 commits of a repository"""
import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    username = sys.argv[2]
    url = 'https://api.github.com'
    req_url = '{}/repos/{}/{}/commits?{}'.format(
            url, username, repo_name, 'per_page=10')
    r = requests.get(
            req_url,
            headers={'Accept': 'application/vnd.github.v3+json'})
    if r.ok:
        [
                print('{}: {}'.format(
                    commit['sha'],
                    commit['commit']['author']['name']))
                for commit in r.json()
        ]
