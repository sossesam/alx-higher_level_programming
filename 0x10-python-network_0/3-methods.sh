#!/bin/bash
# A simple script that gets the body of a redirected request
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-
