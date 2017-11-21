#!/bin/bash
# Displays size of HTTP reponse's message body
curl -sI "$1" | awk '/Content-Length/ { print $2 }'
