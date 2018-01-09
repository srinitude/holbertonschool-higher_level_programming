#!/usr/bin/node
exports.logMe = function (item) {
  if (this.count === undefined) {
    this.count = 0;
  }
  function printIncrement () {
    console.log(`${this.count}: ${item}`);
    this.count++;
  }
  return printIncrement();
};
