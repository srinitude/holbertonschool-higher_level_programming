#!/usr/bin/python3
"""
STAR WARS
"""
if __name__ == "__main__":
    import sys
    import requests

    query = sys.argv[1]
    url = "https://swapi.co/api/people/?search={}".format(query)
    res = requests.get(url)
    people = res.json()

    count = people.get("count")
    print("Number of results: {}".format(count))

    results = people.get("results")
    names = list(map((lambda d: d.get("name")), results))
    for name in names:
        print(name)

    while people.get("next") is not None:
        url = people.get("next")
        res = requests.get(url)
        people = res.json()
        results = people.get("results")
        names = list(map((lambda d: d.get("name")), results))
        for name in names:
            print(name)
