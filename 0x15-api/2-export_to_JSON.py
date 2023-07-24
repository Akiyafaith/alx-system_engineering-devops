#!/usr/bin/python3
""" Python script to export data in the JSON format"""

import json
import requests
import sys

if __name__ == "__main__":
    base_url = 'https://jsonplaceholder.typicode.com/'
    employee_id = sys.argv[1]

    user_data = requests.get(base_url + 'users/{}'.format(employee_id)).json()
    todo_data = requests.get(
        base_url + 'todos',
        params={'userId': employee_id}
    ).json()
   
    json_data = {
        employee_id: [
            {
                "task": task['title'],
                "completed": task['completed'],
                "username": user_data['username']
            }
            for task in todo_data
        ]
     }

    json_filename = '{}.json'.format(employee_id)

    with open(json_filename, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

    print("Data exported to {}".format(json_filename))
