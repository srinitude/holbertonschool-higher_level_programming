#!/usr/bin/node
const arg = process.argv[2];
const num = parseInt(arg);
const result = (function factorial (arg) {
  if (isNaN(arg)) {
    return 1;
  }
  if (arg === 1) {
    return 1;
  }
  return arg * factorial(arg - 1);
})(num);
console.log(result);
