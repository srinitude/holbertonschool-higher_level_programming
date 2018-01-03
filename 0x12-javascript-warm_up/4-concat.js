#!/usr/bin/node
const splitString = Array(3);
splitString[0] = process.argv[2] || 'undefined';
splitString[1] = 'is';
splitString[2] = process.argv[3] || 'undefined';
const sentence = splitString.join(' ');
console.log(sentence);
