#!/usr/bin/node
/* 10. compute and print factorial of argument. */
const arg = process.argv[2];
const num = parseInt(arg, 10);

function fact (a) {
  if (isNaN(a) || a === 0) {
    return 1;
  } else {
    return a * fact(a - 1);
  }
}

console.log(fact(num));
