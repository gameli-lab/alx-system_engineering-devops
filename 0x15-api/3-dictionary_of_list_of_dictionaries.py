#!/usr/bin/python3
"""
This is the API module
"""

from sys import argv
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    todos = requests.get(url + "todos").json()

    persons = {}
    for user in users:
        user_id = user.get("id")
        userdetails = [
            {"username": user.get("name"), "task": t.get(
                "title"), "completed": t.get("completed")}
            for t in [t for t in todos if t.get("userId") == user_id]
        ]
        persons[user_id] = userdetails

    json_str = json.dumps(persons)

    with open('todo_all_employees.json', 'w', newline="") as jsonfile:
        jsonfile.write(json_str)
