#!/usr/bin/node
/* 0. open and print contents of a file and print error object. */

const fs = require('fs');
const source = process.argv[2];

fs.readFile(source, 'utf8', (err, source) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(source);
});
