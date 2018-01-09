#!/usr/bin/node
const { dict } = require('./101-data');
const vals = Object.keys(dict).map(function (key) {
  return dict[key];
});
let uniqueVals = [];
for (let i = 0; i < vals.length; i++) {
  if (!uniqueVals.includes(vals[i])) {
    uniqueVals.push(vals[i]);
  }
}
const newObject = {};
for (let i = 0; i < uniqueVals.length; i++) {
  const val = uniqueVals[i];
  newObject[val] = [];
}
const allKeys = Object.keys(dict);
for (let i = 0; i < allKeys.length; i++) {
  const key = allKeys[i];
  const val = dict[key];
  let newObjectArr = newObject[val];
  if (typeof (newObjectArr) === 'object') {
    newObjectArr.push(key);
  }
}
console.log(newObject);
