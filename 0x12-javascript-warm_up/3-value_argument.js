#!/usr/bin/node
/* 3. print first argument passed to script. */
const arr = process.argv;
const len = arr.length;
if (len === 2) {
  console.log('No argument');
} else if (len === 3) {
  console.log(arr[2]);
}
