#!/usr/bin/python3
""" script gets the information of user from
https://jsonplaceholder.typicode.com/"""


import csv
import json
import requests
import sys


url_prefix = "https://jsonplaceholder.typicode.com/users/"


def main():
    """ main func """
    id_ = sys.argv[1]
    todos_url = url_prefix + id_ + "/todos"
    users_url = url_prefix + id_
    todos = requests.get(todos_url)
    todos_list = todos.json()
    users = requests.get(users_url)
    user_name = users.json().get("username")
    id_ = users.json().get("id")
    file_name = str(users.json().get("id")) + "." + "json"
    dct = {id_: []}
    for item in todos_list:
        res = {}
        res['username'] = user_name
        res['task'] = item.get('title')
        res['completed'] = item.get('completed')
        dct[id_].append(res)
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(dct, f)


if __name__ == "__main__":
    main()
