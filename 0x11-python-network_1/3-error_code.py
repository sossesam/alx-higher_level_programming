#!/usr/bin/python3
"""
Write a Python script that takes in a URL,
sends a request to the URL and displays the body of the
response (decoded in utf-8).
"""

import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    
    try:
        data = urllib.request.urlopen(url)
        data = data.read()
        print(data.decode("utf-8"))
    except urllib.error.URLError as e:
        print(e.code)

