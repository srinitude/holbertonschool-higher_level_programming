#!/usr/bin/python3
"""
Displays value of X-Request-Id found in response header
"""
from urllib.request import urlopen
from sys import argv
from http.client import HTTPResponse

url = argv[1]
with urlopen(url) as response:
    print(response.getheader("X-Request-Id"))
