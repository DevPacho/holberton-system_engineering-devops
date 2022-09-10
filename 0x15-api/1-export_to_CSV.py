#!/usr/bin/python3
"""Using the previous '0-gather_data_from_an_API.py' file, this script
is extended to export data in the CSV format."""

import csv
import requests
from sys import argv

if __name__ == "__main__":

    employee_ID = int(argv[1])
    users = "https://jsonplaceholder.typicode.com/users/{}".format(employee_ID)
    todos_id = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        employee_ID)
    filepath = f"{argv[1]}.csv"

    response_users = requests.get(users).json()
    id = response_users.get("id")
    username = response_users.get("username")

    response_todos = requests.get(todos_id).json()

    with open(f"{filepath}", "w") as file:
        writer = csv.writer(file, delimiter=",", quoting=csv.QUOTE_ALL)

        for task in response_todos:
            tasks_completed = task.get("completed")
            task_title = task.get("title")
            writer.writerow([id, username, tasks_completed, task_title])
