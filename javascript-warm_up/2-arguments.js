#!/usr/bin/node
const args = process.argv;
if (args.length === 2) {
  console.log('No argument');
}
const msg = args.length === 3 ? 'Argument found' : 'Arguments found';
console.log(msg);
