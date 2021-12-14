#!/usr/bin/node
const args = require('process').argv;
function add (a, b) {
  console.log(parseInt(a) + parseInt(b));
}

add(args[2], args[3]);
