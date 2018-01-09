#!/usr/bin/node
const Sq = require('./5-square');
class Square extends Sq {
  constructor (size) {
    super(size);
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
