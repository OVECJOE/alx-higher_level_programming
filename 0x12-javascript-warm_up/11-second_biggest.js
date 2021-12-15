#!/usr/bin/node
const args = require('process').argv;

if (args.length === 2 || args.length === 3) {
  console.log(0);
} else {
  let max = -Infinity; let result = -Infinity;
  for (let i = 2; i < args.length; i++) {
    const value = parseInt(args[i]);
    if (value > max) {
      [result, max] = [max, value];
    } else if (value < max && value > result) {
      result = value;
    }
  }

  console.log(result);
}
