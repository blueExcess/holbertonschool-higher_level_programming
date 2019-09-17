#!/usr/bin/node
/* 3. print first argument passed to script. */
const arr = process.argv[2];
if (arr === undefined) {
  console.log('No argument');
} else {
  console.log(arr);
}
