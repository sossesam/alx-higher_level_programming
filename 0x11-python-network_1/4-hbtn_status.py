#!/usr/bin/python3
""" This module find the highest number """

import requests as req

with req.get("https://alx-intranet.hbtn.io/status") as response:
    content = response.text
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
