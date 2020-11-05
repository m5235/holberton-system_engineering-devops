#!/usr/bin/python3
"""
task 2
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(argv[1])).json()
    todos_list = requests.get(url + "todos",
                              params={"userId": argv[1]}).json()

    with open('{}.json'.format(user_id), 'w') as x:
        json.dump({user_id: [{
                "task": y.get("title"),
                "completed": y.get("completed"),
                "username": y.get("username")
            } for y in todos_list]}, x)
