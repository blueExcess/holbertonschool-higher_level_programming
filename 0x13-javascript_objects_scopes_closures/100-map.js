#!/usr/bin/node
/* 11. import file and use map to multiply all nums in a list. */
const list = require('./100-data').list;
const list2 = list.map((value, index) => value * index);
console.log(list);
console.log(list2);
