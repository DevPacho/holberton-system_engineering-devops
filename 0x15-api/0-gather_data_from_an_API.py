#!/usr/bin/python3
"""Script that, using this 'https://jsonplaceholder.typicode.com', for a
given employee ID, returns information about his/her TODO list progress."""

import requests
from sys import argv

if __name__ == "__main__":

    employee_ID = int(argv[1])
    users = "https://jsonplaceholder.typicode.com/users/{}".format(employee_ID)
    todos_id = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        employee_ID)

    tasks_completed = 0
    total_tasks = 0

    response_todos = requests.get(todos_id).json()

    response_users = requests.get(users).json()
    name = response_users.get("name")

    for data in response_todos:
        total_tasks += 1
        if data.get("completed"):
            tasks_completed += 1

    print("Employee {} is done with tasks({}/{}):".format(
        name, tasks_completed, total_tasks))

    for data in response_todos:
        if data.get("completed"):
            task_title = data.get("title")
            print("\t", task_title)
