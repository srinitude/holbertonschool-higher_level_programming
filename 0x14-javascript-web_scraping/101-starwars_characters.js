#!/usr/bin/node
const request = require('request');
const args = process.argv.slice(2);
const movieId = args[0];
const filmUrl = `https://swapi.co/api/films/${movieId}`;

function characterPromise (character) {
  return new Promise((resolve, reject) => {
    request.get(character, (err, res, body) => {
      if (err) reject(err);
      const characterName = JSON.parse(body).name;
      resolve(characterName);
    });
  });
}

request.get(filmUrl, (err, res, body) => {
  if (err) throw err;
  const characters = JSON.parse(body).characters;
  const promises = [];
  for (let i = 0; i < characters.length; i++) {
    promises.push(characterPromise(characters[i]));
  }
  Promise.all(promises).then((characters) => {
    characters.forEach((character) => {
      console.log(character);
    });
  });
});
