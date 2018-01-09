#!/usr/bin/node
exports.converter = function (base) {
  this.base = base;
  function convertNumber (number) {
    return number.toString(this.base);
  }
  return convertNumber;
};
