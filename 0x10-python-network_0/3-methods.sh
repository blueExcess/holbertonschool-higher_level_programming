#!/bin/bash
# get all methods a server supports
curl "$1" -X OPTIONS -sI | grep "Allow" | cut -d ' ' -f2-
