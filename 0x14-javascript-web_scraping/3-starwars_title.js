#!/usr/bin/node
/* 3. Print title of SW movie with given arg. */

const request = require('request');
const id = process.argv[2];

const url = 'http://swapi.co/api/films/' + id;
request.get(url, (error, response, body) => {
  if (error) throw error;
  console.log(JSON.parse(body).title);
});
