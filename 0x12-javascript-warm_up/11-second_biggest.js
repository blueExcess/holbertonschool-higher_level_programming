#!/usr/bin/node
/* 11. find second-largest argument given. */
const args = process.argv.slice(2);
const len = args.length;
if (len <= 1) {
  console.log(0);
  process.exit();
}

let bigger = parseInt(args[0], 10);
let big = parseInt(args[1], 10);
if (bigger < big) {
  bigger = args[1];
  big = args[0];
}

for (let i = 2; i < len; i++) {
  const x = parseInt(args[i], 10);
  if (bigger < x) {
    big = bigger;
    bigger = x;
  } else if (big < x) {
    big = x;
    }
}
console.log(big);

/* not working properly with floats. */
