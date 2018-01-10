#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const args = process.argv.slice(2);
const url = args[0];
const file = args[1];

request(url).pipe(fs.createWriteStream(file));
