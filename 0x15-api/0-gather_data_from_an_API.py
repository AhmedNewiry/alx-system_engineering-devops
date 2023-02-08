#!/usr/bin/python3
"""A script that, using a RESTful api, for given employee ID,
   returns information about his/her TODO list progress
"""


import requests
import sys


api = 'https://jsonplaceholder.typicode.com'
if __name__ == '__main__':
    emp_id = sys.argv[1]
    user_info = requests.get('{}/users/{}'.format(api, emp_id))
    user_info = user_info.json()
    todos = requests.get('{}/todos?userId={}'.format(api, emp_id))
    todos = todos.json()
    completed_todos = []
    for todo in todos:
        if todo['completed'] is True:
            completed_todos.append(todo)
    print("Employee {} is done with tasks({}/{}):".format(user_info['name'],
          len(completed_todos), len(todos)))
    for todo in completed_todos:
        print("\t {}".format(todo['title'])
