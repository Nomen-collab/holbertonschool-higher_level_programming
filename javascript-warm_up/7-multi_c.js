#!/usr/bin/node
const x = parseInt(process.argv[2]);

if (Number.isNaN(x)) {
  console.log('Missing number of occurrences');
} else if (x > 0) {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
