#!/usr/bin/python3
""" Script using REST API, For a given employee's Id
return the information about his/her TODO list progress"""
import requests
import sys

if __name__ == '__main__':
	base_url = 'https://jsonplaceholder.typicode.com/'
	employee_id = sys.argv[1]

	user_data = requests.get(base_url + 'users/{}'.format(employee_id)).json()
	todo_data = requests.get(base_url + 'todos', params={'userId': employee_id}).json()

	completed_tasks = [task['title'] for task in todo_data if task['completed']]
	total_tasks = len(todo_data)

	print("Employee {} is done with tasks({}/{}):".format(user_data['name'], len(completed_tasks), total_tasks))
	for task in completed_tasks:
		print("\t{}".format(task))
