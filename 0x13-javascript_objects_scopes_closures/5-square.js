#!/usr/bin/node
/* 5. Write class Square that inherits from Rectangle. */

// Rectangle
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

// Square
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }
}

module.exports = Rectangle;
module.exports = Square;
