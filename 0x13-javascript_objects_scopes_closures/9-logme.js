#!/usr/bin/node
/* 9. function that prints num of args printed and new arg value. */

exports.logMe = function (item) {
  if (typeof exports.logMe.count === 'undefined') {
    exports.logMe.count = 0;
  }
  exports.logMe.count += 1;
  console.log(exports.logMe.count + ': ' + item);
};
