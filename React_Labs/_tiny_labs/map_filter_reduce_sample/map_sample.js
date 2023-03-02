// map_sample.js
// -------------
// Sample of using of MAP function

// Execute:
//    node.exe map_sample.js
//    VSCode: CTRL f5

function double(x) {
    return (x * 2);
  }

var numbers = [3, 15, 24, 6];

// Version 1 - Using shorter syntax (calling anonymous function)
var newNumbers = [];
numbers.forEach(function (x) {
    newNumbers.push(x*2);
});
console.log("v2 - Origen: " + numbers + " Result: " + newNumbers);

// Version 3 - Using even shorter syntax (using map function)
var newNumbers = [];
newNumbers = numbers.map(double);
console.log("v3 - Origen: " + numbers + " Result: " + newNumbers);
