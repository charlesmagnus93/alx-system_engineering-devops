#!/usr/bin/python3
"""
Export given user todos into CSV
"""
import requests
import sys


def getUser(id):
    r = requests.get('https://jsonplaceholder.typicode.com/users/' + id)
    return r.json()


def getTodos(userID, done=None):
    url = 'https://jsonplaceholder.typicode.com/users/' + userID + '/todos'

    if done is not None:
        if done:
            url += '?completed=true'
        else:
            url += '?completed=false'
    r = requests.get(url)
    return r.json()


if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.exit(0)

    userID = sys.argv[1]

    if not userID.isnumeric():
        sys.exit(0)

    user = getUser(userID)
    if not user:
        sys.exit(0)

    todos = getTodos(userID)

    file = '{}.csv'.format(userID)

    with open(file, 'a+') as the_file:
        line = '"{}","{}","{}","{}"\n'
        for todo in todos:
            the_file.write(line.format(
                userID,
                user['username'],
                todo['completed'],
                todo['title']))
