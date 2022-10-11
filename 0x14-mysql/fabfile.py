from fabric.api import *
env.hosts=["web-01.cloza.tech", "web-02.cloza.tech"]
def do_copy(file_name):
    put(file_name)
