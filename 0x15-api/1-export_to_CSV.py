#!/usr/bin/python3
""" script gets the information of user from
https://jsonplaceholder.typicode.com/"""


import csv
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
    user_name = '"' + user_name + '"'
    parent = []
    file_name = str(users.json().get("id")) + "." + "csv"
    for item in todos_list:
        ls = []
        user_id = str(item.get("userId"))
        user_id = '"' + user_id + '"'
        ls.append(user_id)
        ls.append(user_name)
        completed = str(item.get("completed"))
        completed = '"' + completed + '"'
        ls.append(completed)
        title = item.get("title")
        title = '"' + title + '"'
        ls.append(title)
        parent.append(ls)
    with open(file_name, "w", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(parent)


if __name__ == "__main__":
    main()
