# Author:zhang
# -*- coding:utf-8 -*-
import time

username = 'alex'
password = '123456'


def auth(auth_type):
    def out_wrapper(func):
        def wrapper(*args, **kwargs):
            name = input("name:").strip()
            passd = input("password:").strip()
            if name == username and password == passd:
                print("\033[32;1m User has passd authentication\033[0m")
                func(*args, **kwargs)
            else:
                print('\033[31;1m\ninvalid username or password\033[0m')

        return wrapper

    return out_wrapper


@auth(auth_type='local')
def index():
    print("welcome to index page")
    return "from home"


def home():
    print("welcome to home page")


def bbs():
    print("welcome to bbs page")


index()
