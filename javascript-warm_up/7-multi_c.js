#!/usr/bin/node
let times = process.argv[2];
if (isNaN(times)) {
  console.log('Missing number of occurrences');
  process.exit(1);
}
for (times; times > 0; times--) {
  console.log('C is fun');
}
