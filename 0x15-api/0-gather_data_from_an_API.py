#!/usr/bin/python3
"""
Get given user ID TODOS
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
    taksCompleted = [todo for todo in todos if todo['completed']]

    print('Employee {} is done with tasks({}/{}):'.format(
        user['name'],
        len(taksCompleted),
        len(todos)))

    for todo in taksCompleted:
        print('\t ' + todo['title'])
