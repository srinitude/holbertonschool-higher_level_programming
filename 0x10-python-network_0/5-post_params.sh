#!/bin/bash
# Sends POST request with request body
curl -sX POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
