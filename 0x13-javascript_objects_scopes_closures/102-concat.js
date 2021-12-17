#!/usr/bin/node
const fs = require('fs');
const args = require('process').argv;

for (let i = 2; i < args.length - 1; i++) {
  const data = fs.readFileSync(args[i], 'utf8');
  fs.writeFileSync(args[args.length - 1], data, { flag: 'a+' });
}
