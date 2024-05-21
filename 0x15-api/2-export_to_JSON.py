#!/usr/bin/python3
"""
This is the API module
"""

from sys import argv
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": argv[1]}).json()

    data = {
        "{}".format(argv[1]): [
            {"task": t.get("title"), "completed": t.get(
                "completed"), "username": user.get("name")}
            for t in todos
        ]
    }

    json_str = json.dumps(data)

    with open('{}.json'.format(argv[1]), 'w', newline="") as jsonfile:
        jsonfile.write(json_str)
