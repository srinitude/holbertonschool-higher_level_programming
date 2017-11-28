#!/usr/bin/python3
"""
Interview
"""
if __name__ == "__main__":
    import sys
    import requests

    repo = sys.argv[1]
    org = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(repo, org)
    res = requests.get(url)
    commits = res.json()
    count = 0
    for commit in commits:
        if count < 10:
            if isinstance(commit, dict):
                sha = commit.get("sha")
                name = commit.get("commit").get("author").get("name")
                print("{}: {}".format(sha, name))
            count += 1
        else:
            break
