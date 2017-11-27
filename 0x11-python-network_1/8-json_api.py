#!/usr/bin/python3
"""
Searches database for users beginning with a certain letter
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    try:
        letter = argv[1]
    except IndexError:
        letter = ""
    query = {}
    query["q"] = letter
    res = requests.post("http://0.0.0.0:5000/search_user",
                        data=query)
    user_id = res.json().get("id")
    name = res.json().get("name")
    if not user_id or not name:
        print("No result")
    else:
        print("[{}] {}".format(user_id, name))
