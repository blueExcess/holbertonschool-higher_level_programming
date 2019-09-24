#!/usr/bin/node
/* 13 (adv). Open and concat two files into a third. */

const fs = require('fs');
const file1 = fs.readFileSync('./fileA', 'utf8');
const file2 = fs.readFileSync('./fileB', 'utf8');
fs.appendFileSync('./fileC', file1, 'utf8');
fs.appendFileSync('./fileC', file2, 'utf8');
