#!/usr/bin/python3
"""
This is the API module
"""

from sys import argv
import json
import requests
import csv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": argv[1]}).json()
    with open("{}.csv".format(argv[1]), "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                         "TASK_TITLE"])
        for t in todos:
            writer.writerow([argv[1], user.get("name"), t.get(
                "completed"), t.get("title")])
