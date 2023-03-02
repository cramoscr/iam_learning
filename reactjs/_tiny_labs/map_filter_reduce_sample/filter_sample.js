// filter_sample.js
// -------------
// Sample of using of FILTER function

// Execute:
//   node.exe filter_sample.js
//   VScode -> CTRL f5

var numbers = [3, 15, 24, 6];

// Version 1 - Using forEach + anonymous function)
var newNumbers = [];
numbers.forEach(function (num) {
    if (num > 10) {
      newNumbers.push(num);
    };
});
console.log("v1 - Origen: " + numbers + " Result: " + newNumbers);

// Version 2 - Using Filter function (return elements when evaluate to True)
var newNumbers = numbers.filter(function (num) {
  return (num > 10);
});
console.log("v3 - Origen: " + numbers + " Result: " + newNumbers);


// Sample 2
const words = ['spray', 'limit', 'elite', 'exuberant', 'destruction', 'present'];
const result = words.filter(word => word.length > 6);
console.log("Sample 2: " + result);
// expected output: Array ["exuberant", "destruction", "present"]