#!/usr/bin/node
const request = require('request');
const url = 'https://swapi.co/api/people/18';

request.get(url, (err, res, body) => {
  if (err) throw err;
  console.log(JSON.parse(body).films.length);
});
