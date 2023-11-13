#!/usr/bin/node
const { argv } = module.require('process');

let i = 2;
let largest = 0;
let secondLargest = 0;

while (argv[i]) {
  let num = parseInt(argv[i]);

  if (num > largest) {
    secondLargest = largest;
    largest = num;
  } else if (num > secondLargest) {
    secondLargest = num;
  } else {
    num = 0;
  }
  i++;
}
console.log(secondLargest);
