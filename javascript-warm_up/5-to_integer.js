#!/usr/bin/node

const inputData = parseInt(process.argv[2]);
console.log(`${isNaN(inputData) ? 'Not a number' : `My number: ${inputData}`}`);
