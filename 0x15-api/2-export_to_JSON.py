#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
from sys import argv
import json

if __name__ == "__main__":

    uid = int(argv[1])
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    """get user """
    for user in users:
        if user.get("id") == uid:
            newUser = user

    lt = []
    """get todo"""
    for todo in todos:
        if todo.get("userId") == uid:
            lt.append(todo)

    diccionario = {}
    listacarechimba = []

    """dictionary"""
    for task in lt:
        nTask = {}
        nTask['task'] = task.get('title')
        nTask['completed'] = task.get('completed')
        nTask['username'] = newUser.get('username')
        listacarechimba.append(nTask)

    diccionario[uid] = listacarechimba

    """json format"""
    with open("{}.json".format(uid), "w") as file:
        json.dump(diccionario, file)
