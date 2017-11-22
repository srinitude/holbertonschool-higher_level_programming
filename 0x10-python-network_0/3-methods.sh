#!/bin/bash
# Display all allowed HTTP methods
curl -sIX OPTIONS "$1" | awk -F': ' '/Allow/ { print $2 }'
