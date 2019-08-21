#!/bin/bash
curl -sI "$1" -X GET | grep "Content-Length" | cut -d ':' -f2 | tr -d ' '
