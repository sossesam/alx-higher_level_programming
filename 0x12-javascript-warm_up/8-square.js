#!/usr/bin/node
const { argv } = module.require('process');

const num = parseInt(argv[2]);

let x = 0;

if (!num) {
  console.log('Missing size');
}

while (x < num) {
  let y = 0;

  while (y < num) {
    process.stdout.write('X');
    y++;
  }
  console.log('');
  x++;
}
