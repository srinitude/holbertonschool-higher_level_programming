#!/usr/bin/python3
"""
Interview
"""
if __name__ == "__main__":
    import requests
    import os

    url = "https://api.github.com/repos/rails/rails/commits"
    res = requests.get(url)
    commits = res.json()
    count = 0
    for commit in commits:
        count += 1
        sha = commit.get("commit").get("tree").get("sha")
        name = commit.get("commit").get("committer").get("name")
        print("{}: {}".format(sha, name))
        if count == 10:
            break
