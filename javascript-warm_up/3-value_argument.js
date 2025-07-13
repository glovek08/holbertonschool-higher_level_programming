#!/usr/bin/node
process.argv[3] === undefined
  ? console.log('No argument')
  : process.argv.slice(2).forEach(arg => console.log(arg));
