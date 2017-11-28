#!/usr/bin/python3
"""
Interview
"""
if __name__ == "__main__":
    import sys
    import requests
    from requests.auth import HTTPBasicAuth
    import os

    repo = sys.argv[1]
    org = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(repo, org)
    user = os.getenv("USERNAME")
    pw = os.getenv("PW")
    res = requests.get(url,
                       auth=HTTPBasicAuth(user, pw))
    commits = res.json()
    for commit in commits:
        sha = commit.get("commit").get("tree").get("sha")
        name = commit.get("commit").get("committer").get("name")
        print("{}: {}".format(sha, name))
