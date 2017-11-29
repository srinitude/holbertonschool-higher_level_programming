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
    for result in results:
        name = result.get("name")
        print(name)
        film_urls = result.get("films")
        for film_url in film_urls:
            film_res = requests.get(film_url).json()
            title = film_res.get("title")
            print("\t{}".format(title))

    while people.get("next") is not None:
        url = people.get("next")
        res = requests.get(url)
        people = res.json()
        results = people.get("results")
        for result in results:
            name = result.get("name")
            print(name)
            film_urls = result.get("films")
            for film_url in film_urls:
                film_res = requests.get(film_url).json()
                title = film_res.get("title")
                print("\t{}".format(title))
