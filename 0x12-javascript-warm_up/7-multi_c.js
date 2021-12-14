#!/usr/bin/node
let x = require('process').argv[2];
x = parseInt(x);
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
