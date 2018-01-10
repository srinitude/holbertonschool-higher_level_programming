#!/usr/bin/node
const args = process.argv.slice(2);
const fs = require('fs');
fs.readFile(args[0], (err, data) => {
  if (err) throw err;
  fs.writeFile(args[2], data, (error) => {
    if (error) throw error;
  });
  fs.readFile(args[1], (err, contents) => {
    if (err) throw err;
    fs.appendFile(args[2], contents, (error) => {
      if (error) throw error;
    });
  });
});
