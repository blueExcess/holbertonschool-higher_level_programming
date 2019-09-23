#!/usr/bin/node
/* 4. add methods for rotating and doubling rectangle. */

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // print representation of rectangle object.
  print () {
    const str = 'X';
    const line = str.repeat(this.width);
    for (let i = 0; i < this.height; i++) {
      console.log(line);
    }
  }

  // rotate width and height.
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  // double width and height of object.
  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
