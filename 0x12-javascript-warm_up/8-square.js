#!/usr/bin/node
const arguments = process.argv;

const num = parseInt(arguments[2]);
let the_x = 'X'

let x = 0;

if (!num) {
    console.log('Missing size')
}

while (x < num) {
    let y = 0
    new_sentence = ''
    while (y < num) {
        process.stdout.write('X');
        y++;
    }
    console.log('');
    x++;
}