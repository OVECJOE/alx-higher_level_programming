#!/usr/bin/node
let size = require('process').argv[2];
size = parseInt(size);
let result = '';

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      result += 'X';
    }
    if (i !== size - 1) {
      result += '\n';
    }
  }
  console.log(result);
}
