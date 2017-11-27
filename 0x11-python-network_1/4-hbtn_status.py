#!/usr/bin/python3
"""
Fetches content using requests package
"""
if __name__ == "__main__":
    import requests

    r = requests.get("https://intranet.hbtn.io/status")
    print("Body response:", end="\n\t")
    print("- type: {}".format(type(r.text)), end="\n\t")
    print("- content: {}".format(r.text))
