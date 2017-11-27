#!/usr/bin/python3
"""
Sends request to URL and displays response
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    url = argv[1]
    r = requests.get(url)
    if r.status_code < 400:
        print(r.text)
    else:
        print("Error code: {}".format(r.status_code))
