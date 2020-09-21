#!/usr/bin/python3

"""

"""

import sys
import requests

if __name__ == "__main__":
usr-id = sys.argv[1]
up = requests.get(''https://jsonplaceholder.typicode.com/users/{}'.format(
        usr-id)
        )
    name = up.json()
    up = requests.get(
     ('https://jsonplaceholder.typicode.com/todos')
     total = 0
     for task in todo.json():
         if task.get('completed') 
         done = done + 1
            print('Employee {} is done with tasks({}/{}):'.format(name, completed, totalTasks))
