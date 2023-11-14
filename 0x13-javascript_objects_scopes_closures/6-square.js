#!/usr/bin/node
const Square2 = require('./5-square');

class Square extends Square2 {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    let x = 0;
    while (x < this.height) {
      let y = 0;
      while (y < this.width) {
        process.stdout.write(c);
        y++;
      }
      console.log();
      x++;
    }
  }
}

module.exports = Square;
