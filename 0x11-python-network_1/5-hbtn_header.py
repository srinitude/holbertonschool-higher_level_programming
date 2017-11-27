#!/usr/bin/python3
"""
Displays value of X-Request-Id found in response header
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    url = argv[1]
    res = requests.get(url)
    print(res.headers.get("X-Request-Id"))
