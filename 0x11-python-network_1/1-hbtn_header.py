#!/usr/bin/python3
""" This module find the highest number """

import urllib.request
import sys


with urllib.request.urlopen(sys.argv[1]) as response:
    x_request_id = response.info()
    print(x_request_id.get("X-Request-Id"))
    



    
