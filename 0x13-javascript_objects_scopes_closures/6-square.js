#!/usr/bin/node
/* 5. Write class Square that inherits from Rectangle. */

class Square extends require('./5-square') {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      const str = c;
      const line = str.repeat(this.width);
      for (let i = 0; i < this.height; i++) {
        console.log(line);
      }
    }
  }
}

module.exports = Square;
