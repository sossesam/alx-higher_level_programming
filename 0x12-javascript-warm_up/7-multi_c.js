#!/usr/bin/node

const arguments = process.argv;

const num = parseInt(arguments[2]);
const sentence = 'C is fun';

let i = 0;

if (!num) {
    console.log('Missing number of occurrences')
}

while (i < num) {
    console.log(sentence);
    i++;
}