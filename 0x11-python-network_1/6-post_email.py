#!/usr/bin/python3
"""
Sends POST request with email to container
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    url = argv[1]
    header = {}
    header['email'] = argv[2]
    r = requests.post(url, data=header)
    print(r.text)
