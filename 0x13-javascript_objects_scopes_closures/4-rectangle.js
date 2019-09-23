#!/usr/bin/node
/* 4. add methods for rotating and doubling rectangle. */

class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print() {
    const str = 'X';
    const line = str.repeat(this.width);
    for (let i = 0; i < this.height; i++) {
      console.log(line);
    }
  }


}

module.exports = Rectangle
