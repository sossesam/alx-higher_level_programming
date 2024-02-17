#!/bin/bash
# A simple script that gets the body of a redirected request
curl -L --max-redirs 5 $1
