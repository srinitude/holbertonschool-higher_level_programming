#!/usr/bin/node
const Rectangle = require('./4-rectangle');
const Square = class extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (typeof (c) === 'undefined') {
      super.print();
      return;
    }
    let xWidth = c.repeat(this.width);
    for (let h = 0; h < this.height; h++) {
      console.log(xWidth);
    }
  }
};
module.exports = Square;