#!/usr/bin/node

function esrever (list) {
  const new_list = [];
  let i = 0;
  while (list[i]) {
    new_list.unshift(list[i]);
    i++;
  }
  return new_list;
}
module.exports = { esrever };
