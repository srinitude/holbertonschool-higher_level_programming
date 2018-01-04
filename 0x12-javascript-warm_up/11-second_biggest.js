#!/usr/bin/node
const args = process.argv.slice(2).map(arg => parseInt(arg));
const sortedArgs = args.sort((a, b) => a < b);
if (sortedArgs.length <= 1) {
  console.log(0);
} else {
  console.log(sortedArgs[1]);
}
