#!/usr/bin/python3
"""
Sends request to URL and displays response
"""
if __name__ == "__main__":
    from urllib.request import Request, urlopen
    from urllib.error import HTTPError
    from sys import argv

    url = argv[1]
    req = Request(url)

    try:
        with urlopen(req) as res:
            print(res.read().decode("utf-8"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
