#!/usr/bin/node

const arguments = process.argv;

const num = parseInt(arguments[2])

if (num) {
    console.log(`My number: ${num}`)
} else {
    console.log("Not a number")
}
