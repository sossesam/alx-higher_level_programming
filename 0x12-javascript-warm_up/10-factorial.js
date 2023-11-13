#!/usr/bin/node

const { argv } = module.require('process');

function factorial (a) {
  if (isNaN(a)) {
    a = 0;
  }

  const num = parseInt(a);
  if (num <= 1) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}
console.log(factorial(argv[2]));
