#!/usr/bin/node
// const num = Math.floor(Number(process.argv[2]));
// console.log(isNaN(num) ? 'Not a number' : `My number: ${num}`);
const args=process.argv.slice(2);
if(isNaN(args[0])){
    console.log("not a number")
}
else{
    console.log(`my number :${parseInt(args[0])}`)
}
