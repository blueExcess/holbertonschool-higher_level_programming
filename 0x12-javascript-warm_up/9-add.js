#!/usr/bin/node
/* 9. write a function that adds two numbers. */
const arg1 = process.argv[2];
const arg2 = process.argv[3];
const num1 = parseInt(arg1, 10);
const num2 = parseInt(arg2, 10);

function add (a, b) {
  // if (!isNaN(a) && !isNaN(b)) {
  //   return a + b;
  // }
  return a + b;
}
console.log(add(num1, num2));
