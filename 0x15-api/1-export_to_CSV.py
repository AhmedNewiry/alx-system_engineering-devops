#!/usr/bin/python3
"""A script that, using a RESTful api, for given employee ID,
   returns information about his/her TODO list progress
"""


import requests
import sys
import cvs

api = 'https://jsonplaceholder.typicode.com'
if __name__ == '__main__':
    emp_id = sys.argv[1]
    file_name = f'{emp_id}.cvs'
    user_info = requests.get('{}/users/{}'.format(api, emp_id))
    user_info = user_info.json()
    todos = requests.get('{}/todos?userId={}'.format(api, emp_id))
    todos = todos.json()
    with open(file_name, mode="w") as cvs_f:
        writer = csv.writer(cvs_f, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL)
    for todo in todos:
        writer.writerow((todo.['userId'], user_info.['username'],
                         todo.['completed'], todo.['title']))
