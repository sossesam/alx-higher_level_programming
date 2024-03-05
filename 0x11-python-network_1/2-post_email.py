#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email, sends a POST request to the 
passed URL with the email as a parameter, and displays the body of the response 
(decoded in utf-8)
"""
import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    values = {"email": str(sys.argv[2])}
    data = urllib.parse.urlencode(values)
    data = data.encode("utf-8")
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        html = response.read()
        html = html.decode("utf-8")
        print(html)
