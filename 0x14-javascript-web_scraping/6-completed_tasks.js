#!/usr/bin/node
const request = require('request');
const args = process.argv.slice(2);
const url = args[0];

const completedTasks = {};
request.get(url, (err, res, body) => {
  if (err) throw err;
  const todos = JSON.parse(body);
  for (let i = 0; i < todos.length; i++) {
    let key = todos[i].userId;
    if (!(key in completedTasks)) {
      completedTasks[key] = 0;
    }
    if (todos[i].completed) {
      completedTasks[key] += 1;
    }
  }
  console.log(completedTasks);
});
