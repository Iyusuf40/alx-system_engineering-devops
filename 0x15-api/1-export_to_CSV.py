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
    parent = []
    file_name = str(users.json().get("id")) + "." + "csv"
    for item in todos_list:
        ls = []
        ls.append(item.get("userId"))
        ls.append(user_name)
        ls.append(item.get("completed"))
        ls.append(item.get("title"))
        parent.append(ls)
    with open(file_name, "w", encoding="utf-8") as f:
        writer = csv.writer(f, 'unix')
        writer.writerows(parent)


if __name__ == "__main__":
    main()
