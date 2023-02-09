#!/usr/bin/python3
"""A script that, using a RESTful api, for given employee ID,
   returns information about his/her TODO list progress
"""


import requests
import sys
import json

api = 'https://jsonplaceholder.typicode.com'
if __name__ == '__main__':
    emp_id = sys.argv[1]
    file_name = f'{emp_id}.json'
    user_info = requests.get('{}/users/{}'.format(api, emp_id))
    user_info = user_info.json()
    todos = requests.get('{}/todos?userId={}'.format(api, emp_id))
    todos = todos.json()
    todos_copy = []
    for todo in todos:
        todo_copy.append(todo)
    emp_todos = {}
    emp_todos[emp_id] = todos_copy
    with open(file_name, mode='w') as json_file:
        json.dump(emp_todos, json_file)
