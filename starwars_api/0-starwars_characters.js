#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

function printCharacters (characters, index) {
  if (index >= characters.length) {
    return;
  }
  request(characters[index], (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }
    console.log(JSON.parse(body).name);
    printCharacters(characters, index + 1);
  });
}

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  printCharacters(JSON.parse(body).characters, 0);
});
