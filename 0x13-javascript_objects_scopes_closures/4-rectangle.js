#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w && h) {
      if (w > 0 && h > 0) {
        this.width = w;
        this.height = h;
      } else {
        return this;
      }
    }
  }

  print () {
    let x = 0;
    while (x < this.height) {
      let y = 0;
      while (y < this.width) {
        process.stdout.write('X');
        y++;
      }
      console.log();
      x++;
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
