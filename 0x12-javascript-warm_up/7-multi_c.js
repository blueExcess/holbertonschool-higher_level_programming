#!/usr/bin/node
/* 7. print phrase x number of times. */
const arg = process.argv[2];
const num = parseInt(arg, 10);

if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
