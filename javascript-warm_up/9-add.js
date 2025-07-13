#!/usr/bin/node
const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);
if (isNaN(a) || isNaN(b)) {
  console.log('NaN');
  process.exit(1);
} else {
  add(a, b);
}
function add (a, b) {
  console.log(a + b);
}
