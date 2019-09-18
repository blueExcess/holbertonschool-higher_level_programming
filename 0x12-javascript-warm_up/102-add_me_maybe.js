#!/usr/bin/node
/* 16 (adv). function that increments and calls another function. */
exports.addMeMaybe = function (number, theFunction) {
  return theFunction(number + 1);
};
