#!/usr/bin/node
const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0);
} else {
  const numbers = args.map(arg => parseInt(arg)).sort((a, b) => b - a);
  console.log(numbers[1]);
}
