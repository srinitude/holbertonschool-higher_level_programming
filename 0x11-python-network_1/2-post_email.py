#!/usr/bin/python3
"""
Sends POST request with email to container
"""
if __name__ == "__main__":
    from urllib.request import Request, urlopen
    from urllib.parse import urlencode
    from sys import argv

    url = argv[1]
    header = {}
    header['email'] = argv[2]
    data = urlencode(header).encode("ascii")
    req = Request(url, data)
    with urlopen(req) as res:
        address = res.read().decode("utf-8")
        print(address)
