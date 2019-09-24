#!/usr/bin/node
/* 2. display the status code of a GET request. */

const request = require('request');
const url = process.argv[2];

request.get(url, function (error, response) {
  if (error) throw error;
  console.log('code: ' + response.statusCode);
});
