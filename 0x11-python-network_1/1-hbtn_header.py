#!/usr/bin/python3
""" This module find the highest number """

import urllib.request
import sys


with urllib.request.urlopen(sys.argv[1]) as response:
    x_request_id = response.headers.get('X-Request-Id')
    if x_request_id:
        print(f"{x_request_id}")
    else:
        print("X-Request-Id header not found in the response.")



    
