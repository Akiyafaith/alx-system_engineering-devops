#!/usr/bin/python3
""" script using REST API, for a given employee's id,
display the information about his/her TODO list progress
Export data in CSV format
"""

import csv
import requests
import sys

if __name__ == '__main__':
    base_url = 'https://jsonplaceholder.typicode.com/'
    employee_id = sys.argv[1]

    user_data = requests.get(base_url + 'users/{}'.format(employee_id)).json()
    todo_data = requests.get(
        base_url + 'todos',
        params={'userId': employee_id}
    ).json()

    csv_filename = '{}.csv'.format(employee_id)

    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for task in todo_data:
            csv_writer.writerow([
                user_data['id'],
                user_data['username'],
                task['completed'],
                task['title']
            ])
    print("Data exported to {}".format(csv_filename))
