#!/usr/bin/node
const numOfArgs = process.argv.length - 2;
if (numOfArgs === 0) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
