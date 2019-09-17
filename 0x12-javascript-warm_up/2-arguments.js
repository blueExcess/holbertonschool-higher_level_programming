#!/usr/bin/node
/* 2. Print different output based on num of args given. */
const arr = process.argv;
const len = arr.length;
if (len === 2) {
  console.log('No argument');
} else if (len === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
