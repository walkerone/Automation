# Author:zhang
# -*- coding:utf-8 -*-
import configparser

config = configparser.ConfigParser()
config.rem
config["defaule"] = {
    "serverlivealive": 45,
    "Compression": "yes"
}
config["bitbucket.org"] = {}
config["bitbucket.org"]["User"] = "HG"

with open("exmaple.ini", 'w') as configfile:
    config.write(configfile)
config.read("exmaple.ini")

print(config.defaults())
print(config["defaule"]["compression"])