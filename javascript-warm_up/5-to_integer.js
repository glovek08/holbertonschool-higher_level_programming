#!/usr/bin/node
console.log(
  `${
    !Number(parseInt(process.argv[2]))
      ? 'Not a number'
      : `My number: ${parseInt(process.argv[2])}`
  }`
);
