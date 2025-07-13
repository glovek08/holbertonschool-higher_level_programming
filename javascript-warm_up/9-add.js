#!/usr/bin/env node
const a = +process.argv[2];
const b = +process.argv[3];
a != a || b != b
  ? (process.stdout.write("NaN"), process.exit(1))
  : process.stdout.write(a + b);
