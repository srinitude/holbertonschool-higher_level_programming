#!/usr/bin/node
const request = require('request');
const args = process.argv.slice(2);
const episodeId = args[0];
const url = `http://swapi.co/api/films/${episodeId}`;

request.get(url, (error, res, body) => {
  if (error) throw error;
  console.log(JSON.parse(body).title);
});
