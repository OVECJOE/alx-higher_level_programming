#!/usr/bin/node
const args = require('process').argv;
let myVar = parseInt(args[2]);
if (!isNaN(myVar)) {
	console.log(myVar);
}
else {
	console.log('Not a number');
}
