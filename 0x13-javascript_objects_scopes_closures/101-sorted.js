#!/usr/bin/node
/* 12. reverse a dictionary?
IDK, it's kind of weird, and this code is a mess. */

const data = require('./101-data').dict;
const dict = {};
const valueSet = new Set([]);

for (const key in data) {
  valueSet.add(data[key]);
}

function setDict (value) {
  dict[value] = [];
}

valueSet.forEach(setDict);
const keys = Object.keys(data);

function setKey (key) {
  dict[data[key]].push(key);
}
keys.forEach(setKey);
console.log(dict);
