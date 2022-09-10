#!/usr/bin/python3
"""Using the previous '0-gather_data_from_an_API.py' file, this script
is extended to export data in the JSON format."""

import json
import requests
from sys import argv

if __name__ == "__main__":

    employee_ID = int(argv[1])
    users = "https://jsonplaceholder.typicode.com/users/{}".format(employee_ID)
    todos_id = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        employee_ID)
    filepath = "{}.json".format(employee_ID)

    response_users = requests.get(users).json()
    id = response_users.get("id")
    username = response_users.get("username")

    response_todos = requests.get(todos_id).json()

    with open(filepath, "w") as file:
        data_to_export = []

        for task in response_todos:
            tasks_completed = task.get("completed")
            task_title = task.get("title")

            tasks_formatted = {"task": task_title, "completed": tasks_completed, 
                                "username": username}
            data_to_export.append(tasks_formatted)

        data_in_json = {id: data_to_export}
        file.write(json.dumps(data_in_json))
