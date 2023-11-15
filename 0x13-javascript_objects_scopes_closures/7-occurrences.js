#!/usr/bin/node

function nbOccurences (list, element) {
  let count = 0;
  let i = 0;
  while (list[i]) {
    if (list[i] === element) {
      count++;
    }
    i++;
  }
  return count;
}

module.exports = { nbOccurences };
