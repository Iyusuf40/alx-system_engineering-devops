#!/usr/bin/python3
""" script gets the information of user from
https://jsonplaceholder.typicode.com/"""


import csv
import json
import requests


url_prefix = "https://jsonplaceholder.typicode.com/"


def main():
    """ main func """
    todos_url = url_prefix + "todos"
    users_url = url_prefix + "users"
    todos = requests.get(todos_url)
    todos_list = todos.json()
    users = requests.get(users_url)
    users_list = users.json()
    users_dict = {}
    for user in users_list:
        users_dict[user.get("id")] = user.get("username")
    file_name = "todo_all_employees.json"
    dct = {}
    for item in todos_list:
        res = {}
        if not dct.get(item.get('userId')):
            dct[item.get('userId')] = []
        res['username'] = users_dict.get(item.get('userId'))
        res['task'] = item.get('title')
        res['completed'] = item.get('completed')
        dct[item.get('userId')].append(res)
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(dct, f)


if __name__ == "__main__":
    main()
