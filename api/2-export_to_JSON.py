#!/usr/bin/python3
"""Export an employee's TODO list data to a JSON file using a REST API.

Usage: ./2-export_to_JSON.py EMPLOYEE_ID
Creates USER_ID.json with the format:
{"USER_ID": [{"task": "TASK_TITLE", "completed": STATUS,
"username": "USERNAME"}, ...]}
"""
import collections
import json
import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    employee_id = int(sys.argv[1])

    user = requests.get("{}/users/{}".format(base_url, employee_id)).json()
    todos = requests.get(
        "{}/todos".format(base_url), params={"userId": employee_id}
    ).json()

    username = user.get("username")

    tasks = []
    for task in todos:
        item = collections.OrderedDict()
        item["task"] = task.get("title")
        item["completed"] = task.get("completed")
        item["username"] = username
        tasks.append(item)

    with open("{}.json".format(employee_id), "w") as json_file:
        json.dump({str(employee_id): tasks}, json_file)
