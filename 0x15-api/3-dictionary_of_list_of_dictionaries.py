#!/usr/bin/python3
"""Using the previous '0-gather_data_from_an_API.py' file, this script
is extended to export data in JSON format for all the employees in the API."""

import json
import requests
from sys import argv

if __name__ == "__main__":

    users = "https://jsonplaceholder.typicode.com/users/"
    todos_id = "https://jsonplaceholder.typicode.com/todos"
    filepath = "todo_all_employees.json"

    response_users = requests.get(users).json()
    # id = response_users.get("id")
    # username = response_users.get("username")

    response_todos = requests.get(todos_id).json()

    with open(filepath, "w") as file:

        for users_data in response_users:
            data_to_export = []
            username = users_data.get("username")

            for task in response_todos:
                tasks_completed = task.get("completed")
                task_title = task.get("title")

                if task.get("userId") == users_data.get("id"):
                    data_formatted = {"username": username, "task": task_title,
                                      "completed": tasks_completed}
                    data_to_export.append(data_formatted)

            data_in_json = {}
            data_in_json[users_data.get("id")] = data_to_export
        file.write(json.dumps(data_in_json))
