#!/bin/bash
# Script to get content length of curl thingy
curl -sI "$1" -X GET | grep "Content-Length" | cut -d ':' -f2 | tr -d ' '
