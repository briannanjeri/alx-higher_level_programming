#!/usr/bin/node
const number = process.argv.length;
console.log(number === 2 ? 'No argument' : number === 3 ? 'Argument found' : 'Arguments found');
