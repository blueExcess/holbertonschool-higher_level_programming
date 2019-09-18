#!/usr/bin/node
/* 15 (adv). write function that executes a given function n times. */
exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
