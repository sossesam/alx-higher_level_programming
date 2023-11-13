#!/usr/bin/node

const arguments = process.argv;

if (arguments[2]) {
  console.log(arguments[2]);
} else {
    console.log("No argument")
}
