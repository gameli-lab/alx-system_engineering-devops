#!/usr/bin/python3
"""
This is the API module
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": argv[1]}).json()
    num_done = len([t for t in todos if t.get("completed") is True])
    num_total = len(todos)
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), num_done, num_total))
    [print("\t {}".format(t.get("title"))) for t in todos if t.get(
        "completed") is True]
