#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
from sys import argv
import json

if __name__ == "__main__":

    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    putos_users = {}
    puto_name = {}

    """get username"""
    for puto in users:
        uId = puto.get('id')
        putos_users[uId] = []
        puto_name[uId] = puto.get('username')

    """get other features"""
    for task in todos:
        nTask = {}
        uId = task.get('userId')
        nTask['task'] = task.get('title')
        nTask['completed'] = task.get('completed')
        nTask['username'] = puto_name.get(uId)
        putos_users[uId].append(nTask)

    """json format"""
    with open("todo_all_employees.json", "w") as file:
        json.dump(putos_users, file)
