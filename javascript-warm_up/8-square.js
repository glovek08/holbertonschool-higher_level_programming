#!/usr/bin/node

const n = parseInt(process.argv[2]);

if (isNaN(n)) {
  console.log('Missing size');
  process.exit(1);
}
let sqLen = n;
const SYMBOL = 'X';
const LINE = `${SYMBOL.repeat(sqLen)}\n`;

while (sqLen !== 0) {
  process.stdout.write(LINE);
  sqLen--;
}
