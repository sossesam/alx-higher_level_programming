#!/usr/bin/node

const arguments = process.argv;

function factorial(a){
    
    if (isNaN(a)){
        a = 0;
    }

    num = parseInt(a)
    if (num <= 1){
        return 1;
    } else{
        return num * factorial(num - 1)
    }
}
console.log(factorial(arguments[2]))