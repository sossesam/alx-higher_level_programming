#!/usr/bin/node

function esrever (list) {
  const newList = [];
  let i = 0;
  while (list[i]) {
    newList.unshift(list[i]);
    i++;
  }
  return newList;
}
module.exports = { esrever };
