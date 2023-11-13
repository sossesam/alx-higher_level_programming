#!/usr/bin/node

const { argv } = module.require('process');

const num = parseInt(argv[2]);
const sentence = 'C is fun';

let i = 0;

if (!num) {
  console.log('Missing number of occurrences');
}

while (i < num) {
  console.log(sentence);
  i++;
}
