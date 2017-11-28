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
    if commits:
        for commit in commits:
            if type(commit) is dict:
                sha = commit.get("sha")
                name = commit.get("commit").get("author").get("name")
                count += 1
                print("{}: {}".format(sha, name))
                if count == 10:
                    break
