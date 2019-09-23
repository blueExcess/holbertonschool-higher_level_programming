#!/usr/bin/node
/* 10. func that converts from one base to another passed as seperate args. */

exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};
