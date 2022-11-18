#!/usr/bin/python3
"""
    Python script that returns information using a REST API
"""

from sys import argv
import requests


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    userId = argv[1]
    user_info = requests.get(f"{url}users/{userId}").json()
    employee_name = user_info.get('name')
    all_tasks = requests.get(f"{url}todos?userId={userId}").json()
    completed_tasks = []
    for task in all_tasks:
        if task.get('completed'):
            completed_tasks.append(task)

    print('Employee {} is done with tasks({}/{}):'
          .format(employee_name, len(completed_tasks),
                  len(all_tasks)))

    for task in completed_tasks:
        print(f"\t {task.get('title')}")
