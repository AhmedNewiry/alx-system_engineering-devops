#!/usr/bin/python3
"""A script that, using a RESTful api, for given employee ID,
   returns information about his/her TODO list progress
"""

import json
import requests
import sys

api = 'https://jsonplaceholder.typicode.com'
if __name__ == '__main__':
    emp_id = sys.argv[1]
    file_name = '{}.json'.format(emp_id)
    user_info = requests.get('{}/users/{}'.format(api, emp_id))
    user_info = user_info.json()
    todos = requests.get('{}/todos?userId={}'.format(api, emp_id))
    todos = todos.json()
    emp_todos = {}
    todos_copy = []
    for todo in todos:
        task = {'task': todo.get('title'),
                'completed': todo.get('completed'),
                'username': user_info.get('username')
                }
        todos_copy.append(task)
    emp_todos[str(emp_id)] = todos_copy
    with open(file_name, mode='w') as json_file:
        json.dump(emp_todos, json_file)
