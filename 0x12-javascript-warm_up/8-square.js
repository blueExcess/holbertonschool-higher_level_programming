#!/usr/bin/node
/* 8. Print a square */
const arg = process.argv[2];
const num = parseInt(arg, 10);
if (isNaN(num)) {
  console.log('Missing size');
} else {
  const str = 'X';
  const line = str.repeat(num);
  for (let i = 0; i < num; i++) {
    console.log(line);
  }
}
