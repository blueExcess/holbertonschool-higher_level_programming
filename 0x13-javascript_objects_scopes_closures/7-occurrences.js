#!/usr/bin/node
/* write a function that returns number of occurances in a list. */

exports.nbOccurences = function (list, searchElement) {
  count = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      count += 1;
    }
  }
  return count;
}
