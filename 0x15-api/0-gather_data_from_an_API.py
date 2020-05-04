#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
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

    print("Employee {} is done with tasks({}/{}):".format(newUser.get('name'),
                                                          len(full_tasks),
                                                          len(lt)))

    for title in full_tasks:
        print("\t {}".format(title.get('title')))
