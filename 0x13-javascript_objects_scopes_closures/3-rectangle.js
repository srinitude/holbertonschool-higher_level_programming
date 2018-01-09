#!/usr/bin/node
const Rectangle = class {
  constructor (w, h) {
    if (typeof (w) === 'undefined' || typeof (h) === 'undefined') {
      return;
    }
    if (w <= 0 || h <= 0) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    let xWidth = 'X'.repeat(this.width);
    for (let h = 0; h < this.height; h++) {
      console.log(xWidth);
    }
  }
};
module.exports = Rectangle;
