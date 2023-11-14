#!/usr/bin/node

function callMeMoby (a, theFunction) {
  let i = 0;

  while (i < a) {
    theFunction();
    i++;
  }
}

module.exports = { callMeMoby };
