#!/usr/bin/python3
"""Export the TODO list data of all employees to a JSON file using a REST API.

Usage: ./3-dictionary_of_list_of_dictionaries.py
Creates todo_all_employees.json with the format:
{"USER_ID": [{"username": "USERNAME", "task": "TASK_TITLE",
"completed": STATUS}, ...], ...}
"""
import collections
import json
import requests


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"

    users = requests.get("{}/users".format(base_url)).json()
    todos = requests.get("{}/todos".format(base_url)).json()

    all_data = collections.OrderedDict()
    for user in users:
        user_id = user.get("id")
        tasks = []
        for task in todos:
            if task.get("userId") == user_id:
                item = collections.OrderedDict()
                item["username"] = user.get("username")
                item["task"] = task.get("title")
                item["completed"] = task.get("completed")
                tasks.append(item)
        all_data[str(user_id)] = tasks

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_data, json_file)
