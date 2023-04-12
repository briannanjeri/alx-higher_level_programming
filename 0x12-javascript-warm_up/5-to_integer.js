#!/usr/bin/node
const args=process.argv.slice(2);
if(isNaN(args[0])){
    console.log("not a number")
}
else{
    console.log(`my number :${parseInt(args[0])}`)
}
