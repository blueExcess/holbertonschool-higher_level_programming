#!/usr/bin/node
/* 13 (adv). Open and concat two files into a third. */

const fs = require('fs');
const args = process.argv.slice(2);

const sourceA = args[0];
const sourceB = args[1];
const dest = args[2];
const file1 = fs.readFileSync(sourceA, 'utf8');
const file2 = fs.readFileSync(sourceB, 'utf8');
fs.appendFileSync(dest, file1, 'utf8');
fs.appendFileSync(dest, file2, 'utf8');
