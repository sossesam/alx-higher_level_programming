#!/bin/bash
# A simple script that gets the body of a redirected request
curl -so /dev/null -w "%{http_code}" "$1"
