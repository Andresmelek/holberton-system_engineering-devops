#!/usr/bin/python3
"""
Python script to export data in the CSV format.
"""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    uid = int(argv[1])
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    for user in users:
        if user.get("id") == uid:
            newUser = user

    lt = []
    for todo in todos:
        if todo.get("userId") == uid:
            lt.append(todo)

    full_tasks = []
    for task in lt:
        if task.get('completed') is True:
            full_tasks.append(task)

    with open(("{}.csv").format(uid), 'w') as file:
        data = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
        for task in lt:
            data.writerow([uid, newUser.get('username'),
                          task.get('completed'), task.get('title')])
