#!/bin/bash
# A simple script that gets the body of a redirected request
curl -sH "X-School-User-Id: 98" "${1}"
