#!/usr/bin/node
function factorial (n) {
  if (Number.isNaN(n) || n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}

const num = parseInt(process.argv[2]);

if (Number.isNaN(num)) {
  console.log(1);
} else if (num < 0) {
  // Ne rien afficher pour les nombres négatifs, comme dans l'exemple './10-factorial.js -3'
} else {
  console.log(factorial(num));
}
