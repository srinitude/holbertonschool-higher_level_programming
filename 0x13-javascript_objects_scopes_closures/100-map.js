#!/usr/bin/node
const { list } = require('./100-data.js');
const mappedList = list.map((current, index) => {
  return current * index;
});
console.log(list);
console.log(mappedList);
