#!/usr/bin/node

const arguments = process.argv;

function add(a,b) {

    console.log(a + b)
}

add(parseInt(arguments[2]), parseInt(arguments[3]))