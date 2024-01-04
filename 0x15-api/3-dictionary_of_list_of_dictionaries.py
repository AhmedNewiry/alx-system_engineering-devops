#!/usr/bin/python3
"""A script that, using a RESTful api, for given employee ID,
   returns information about his/her TODO list progress
"""


import json
import requests
import sys

api = 'https://jsonplaceholder.typicode.com'
if __name__ == '__main__':
    file_name = 'todo_all_employees.json'
    users = requests.get('{}/users/'.format(api))
    users = users.json()
    emp_todos = {}
    for usr in users:
        emp_id = usr['id']
        todos = requests.get('{}/todos?userId={}'.format(api, emp_id))
        todos = todos.json()
        todos_copy = []
        for todo in todos:
            task = {'username': usr['name'],
                    'task': todo['title'],
                    'completed': todo['completed']
                    }
            todos_copy.append(task)
        emp_todos[str(emp_id)] = todos_copy
    with open(file_name, mode='w') as json_file:
        json.dump(emp_todos, json_file)
