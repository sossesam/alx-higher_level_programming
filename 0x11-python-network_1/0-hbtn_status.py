#!/usr/bin/python3
""" This module find the highest number """

import urllib.request as req

with req.urlopen("https://alx-intranet.hbtn.io/status") as response:
    content = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
    print("\t- utf8 content: {}".format(content.decode('utf-8')))
