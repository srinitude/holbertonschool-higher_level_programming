#!/usr/bin/python3
"""
STAR WARS
"""
if __name__ == "__main__":
    import sys
    import requests

    query = sys.argv[1]
    payload = {}
    payload["search"] = query
    base_url = "https://swapi.co/api/people/"
    res = requests.get(base_url, params=payload)
    people = res.json()
    results = people.get("results")
    count = len(results)
    names = list(map((lambda d: d.get("name")), results))

    print("Number of results: {}".format(count))
    for name in names:
        print(name)
