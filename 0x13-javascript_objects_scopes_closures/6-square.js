#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (typeof (c) === 'undefined') {
      super.print();
    } else {
      let xWidth = c.repeat(this.width);
      for (let h = 0; h < this.height; h++) {
	console.log(xWidth);
      }
    }
  }
}
const square = Square;
module.exports = square;
