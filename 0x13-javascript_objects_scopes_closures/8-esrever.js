#!/usr/bin/node
/* 8. function to reverse a given list */

exports.esrever = function (list) {
  const ret = [];
  while (list.length) {
    ret.push(list.pop());
  }
  return ret;
};
