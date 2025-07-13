#!/usr/bin/env node
const args = process.argv;
if (args.length < 4) {
  console.log(0);
  process.exit(1);
}
let max = -Infinity;
let secondMax = -Infinity;
for (let i = 2; i < args.length; i++) {
  const num = +args[i];
  if (num > max) {
    secondMax = max;
    max = num;
  } else if (num > secondMax && num < max) {
    secondMax = num;
  }
}
console.log(secondMax);
