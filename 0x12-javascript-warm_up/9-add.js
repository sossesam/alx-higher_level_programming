#!/usr/bin/node

const { argv } = module.require('process');

function add (a, b) {
  console.log(a + b);
}

add(parseInt(argv[2]), parseInt(argv[3]));
