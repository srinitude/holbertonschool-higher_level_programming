#!/bin/bash
# Displays size of HTTP reponse's message body
curl -s -o /dev/null -w "%{size_download}\n" "$1"
