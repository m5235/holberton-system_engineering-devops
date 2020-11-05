#!/usr/bin/python3
"""
Task three
"""
import json
import requests
import sys

if __name__ == "__main__":

    file_name = 'todo_all_employees.json'
    # write json
    with open(file_name, "w") as json_file:
        r = requests.get('https://jsonplaceholder.typicode.com/users/')
        x = 0
        my_employees = {}
        for user in r.json():
            user_id = r.json()[x]['id']
            username = r.json()[x]['username']
            r2 = requests.get(
                    'https://jsonplaceholder.typicode.com/users/{}/todos'
                    .format(
                        user_id)
                    )
            my_employees[str(user_id)] = []
            for task in r2.json():
                dicti = {}
                dicti["username"] = username
                dicti["task"] = task["title"]
                dicti["completed"] = task["completed"]
                my_employees[str(user_id)].append(dicti)
            x = x + 1
        json.dump(my_employees, json_file)
