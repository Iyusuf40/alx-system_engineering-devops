#!/usr/bin/python3
""" script gets the information of user from
https://jsonplaceholder.typicode.com/"""


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
    size = len(todos_list)
    completed = 0
    completed_tasks_title = ""
    for item in todos_list:
        if item.get("completed"):
            completed += 1
            completed_tasks_title = completed_tasks_title + "\t " +\
                item.get("title") + "\n"

    ratio = str(completed) + "/" + str(size)
    users = requests.get(users_url)
    name = users.json().get("name")

    if (size):
        print("Employee {} is done with tasks({}):".format(name, ratio))
    print(completed_tasks_title, end="")


if __name__ == "__main__":
    main()
