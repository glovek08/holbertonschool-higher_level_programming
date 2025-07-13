#!/usr/bin/node
const a = process.argv[2];
const b = process.argv[3];
if (isNaN(a) || isNaN(b)) {
  process.stdout.write('NaN\n');
  process.exit(1);
} else {
  add(a, b);
}
function add (a, b) {
  process.stdout.write(a + b + '\n');
}
