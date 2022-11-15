#!/usr/bin/python3
"""
Get given user ID TODOS
"""

if __name__ == "__main__":
	import requests
	import sys

	def getUser(id):
		res = requests.get('https://jsonplaceholder.typicode.com/users/' + id)
		return res.json()

	def getTodos(userID, taskDone=None):
		url = 'https://jsonplaceholder.typicode.com/users/' + userID + '/todos'

		if taskDone is not None:
			if taskDone:
				url += '?completed=true'
			else:
				url	 += '?completed=false'

		res = requests.get(url)
		return res.json()

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

		print('Employee {} is done with tasks({}):'.format(
			user['name'],
			len(taksCompleted),
			len(todos)
		))

		for todo in taksCompleted:
			print('\t' + todo['title'])

