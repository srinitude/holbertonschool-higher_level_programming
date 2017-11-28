#!/usr/bin/python3
"""
Retrieve Github ID
"""
if __name__ == "__main__":
    import sys
    import requests
    from requests.auth import HTTPBasicAuth

    base_url = "https://api.github.com/users/"
    full_url = "{}{}".format(base_url, sys.argv[1])
    res = requests.get(full_url,
                       auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    if res.status_code != 200:
        print(None)
        sys.exit()
    print(res.json().get("id"))
