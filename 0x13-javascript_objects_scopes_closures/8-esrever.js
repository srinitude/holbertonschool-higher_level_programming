#!/usr/bin/node
exports.esrever = function (list) {
  const listLength = list.length;
  let listCopy = Array(listLength);
  const lastIdx = listLength - 1;
  for (let i = 0; i < listLength; i++) {
    listCopy[i] = list[lastIdx - i];
  }
  return listCopy;
};
