#!/usr/bin/python3
"""
This is the API module
"""

import csv
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": argv[1]}).json()
    with open("{}.csv".format(argv[1]), "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for t in todos:
#            writer.writerow(['"{0}"'.format(argv[1]), '"{0}"'.format(user.get("name")), '"{0}"'.format(t.get("completed")), '"{0}"'.format(t.get("title"))])
            writer.writerow(['"{0}","{1}","{2}","{3}"'.format(argv[1], user.get("name"), t.get("completed"), t.get("title"))])

