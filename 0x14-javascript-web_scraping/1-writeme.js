#!/usr/bin/node
const args = process.argv.slice(2);
const fs = require('fs');
fs.writeFile(args[0], args[1], 'utf-8', (error) => {
  if (error) console.log(error);
});
