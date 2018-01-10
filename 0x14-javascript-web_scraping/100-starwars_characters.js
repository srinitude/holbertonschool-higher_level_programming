#!/usr/bin/node
const request = require('request');
const args = process.argv.slice(2);
const movieId = args[0];
const filmUrl = `https://swapi.co/api/films/${movieId}`;

request.get(filmUrl, (err, res, body) => {
  if (err) throw err;
  const characters = JSON.parse(body).characters;
  for (let i = 0; i < characters.length; i++) {
    request.get(characters[i], (err, res, body) => {
      if (err) throw err;
      const characterName = JSON.parse(body).name;
      console.log(characterName);
    });
  }
});
