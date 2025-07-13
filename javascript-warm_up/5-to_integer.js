#!/usr/bin/node
console.log(
  `My number: ${
    !Number(parseInt(process.argv[2]))
      ? 'Not a number'
      : parseInt(process.argv[2])
  }`
);
