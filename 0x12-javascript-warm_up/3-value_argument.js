#!/usr/bin/node
let numOfArgs = 0;
process.argv.forEach((element) => { numOfArgs++; });
if (numOfArgs === 2) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
