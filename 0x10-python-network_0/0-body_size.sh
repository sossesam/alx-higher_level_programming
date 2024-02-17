#!/bin/bash

# A simple script to get the size of a request

curl -sI $1|grep "Content-Length:"| cut -d " " -f 2
