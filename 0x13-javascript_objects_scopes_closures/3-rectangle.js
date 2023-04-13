#!/usr/bin/node
module.exports = class Rectangle {
    constructor(w,h){
        if(w>0 && h>0){
            [this.width, this.height]=[w,h]
        }
    }
  print() {
        let row = "";
        for (let i = 0; i < this.height; i++) {
            row += "X".repeat(this.width) + "\n";
        }
        console.log(row);
    }

}
