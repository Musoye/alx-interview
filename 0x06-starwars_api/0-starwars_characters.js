#!/usr/bin/node
// star wars api
const request = require('request');

const star = (url) => {
  request(url, (error, response, body) => {
    if (error) {
      throw error;
    }
    const characters = JSON.parse(body);
    const people = characters.characters;
    for (const character of people) {
      request(character, (error, response, body) => {
        if (error) {
          throw error;
        }
        const person = JSON.parse(body);
        console.log(person.name);
      });
    }
  });
};

const value = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + value;
star(url);
