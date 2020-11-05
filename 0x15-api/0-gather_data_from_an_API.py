#!/usr/bin/python3

"""
task 0
"""

import requests
import sys

if __name__ == "__main__":
    Myurl = "https://jsonplaceholder.typicode.com/"

    user_id = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos_list = requests.get(url + "todos",
                              params={"userId": sys.argv[1]}).json()

    progress = [t.get("title") for t in todos_list
                if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(progress), len(todos_list)))

    for i in progress:
        print("\t {}".format(i))
