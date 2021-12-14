#!/usr/bin/node
const args = require('process').argv;
const myVar = parseInt(args[2]);
if (!isNaN(myVar)) {
  console.log('My number: ' + myVar);
} else {
  console.log('Not a number');
}
