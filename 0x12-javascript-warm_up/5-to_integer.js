#!/usr/bin/node
/* 5. print if can be converted to int. */
const args = process.argv[2];
const parse = parseInt(args, 10);

if (isNaN(parse)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parse);
}
