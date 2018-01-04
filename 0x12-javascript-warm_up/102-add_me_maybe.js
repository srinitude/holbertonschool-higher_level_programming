#!/usr/bin/node
exports.addMeMaybe = (num, fn) => {
  ++num;
  fn(num);
};
