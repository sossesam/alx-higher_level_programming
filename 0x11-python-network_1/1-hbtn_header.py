#!/usr/bin/python3
""" This module find the highest number """

import urllib.request
import sys


with urllib.request.urlopen(sys.argv[1]) as response:
    x_request_id = response.info()
    if x_request_id:
        print(x_request_id.get("X-Request-Id"))
    else:
        print("X-Request-Id header not found in the response.")



    
