#!/usr/bin/python3
"""
Export JSON all employees todos
"""
import json
import requests
import sys


def getAllUsers(id=None):
    url = 'https://jsonplaceholder.typicode.com/users'
    if id is not None:
        url += '/' + id
    r = requests.get(url)
    return r.json()


def getAllTodos(userID, done=None):
    url = 'https://jsonplaceholder.typicode.com/users/' + userID + '/todos'
    if done is not None:
        if done:
            url += '?completed=true'
        else:
            url += '?completed=false'
    r = requests.get(url)
    return r.json()


if __name__ == '__main__':
    users = getAllUsers()

    file = 'todo_all_employees.json'

    jsonData = {}
    for user in users:
        jsonData[user['id']] = []
        todos = getAllTodos(str(user['id']))
        for todo in todos:
            jsonData[user['id']].append({
                'username': user['username'],
                'task': todo['title'],
                'completed': todo['completed']})

    with open(file, 'w+') as the_file:
        json.dump(jsonData, the_file)
