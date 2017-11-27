#!/usr/bin/python3
"""
Makes request to Holberton's status page using urllib package
"""
from urllib.request import Request, urlopen

req = Request("https://intranet.hbtn.io/status")
with urlopen(req) as res:
    html = res.read()
    print("Body response:", end="\n\t")
    print("- type: {}".format(type(html)), end="\n\t")
    print("- content: {}".format(html), end="\n\t")
    print("- utf8 content: {}".format(html.decode("utf-8")))
