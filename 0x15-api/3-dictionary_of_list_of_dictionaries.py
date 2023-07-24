#!/usr/bin/python3
"""a Python script to export data in the JSON format"""

import json
import requests
import sys

if __name__ == "__main__":
    base_url = 'https://jsonplaceholder.typicode.com/'

    all_todo_data = {}
    for employee_id in range(1, 11):
        user_data = requests.get(
            base_url + 'users/{}'.format(employee_id)
        ).json()
        todo_data = requests.get(
            base_url + 'todos',
            params={'userId': employee_id}
        ).json()

        tasks = [
            {
                "username": user_data['username'],
                "task": task['title'],
                "completed": task['completed']
            }
            for task in todo_data
        ]

        all_todo_data[str(employee_id)] = tasks
    json_filename = 'todo_all_employees.json'

    with open(json_filename, 'w') as json_file:
        json.dump(all_todo_data, json_file, indent=4)
    print("Data exported to {}".format(json_filename))
