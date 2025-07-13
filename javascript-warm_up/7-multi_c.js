#!/usr/bin/node
const n = +process.argv[2];
if (!Number.isInteger(n) || n < 1) {
  console.log('Missing number of occurrences');
  process.exit(1);
}
// precomputing
const line = 'C is fun\n';
const output = line.repeat(n);
process.stdout.write(output);
