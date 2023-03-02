// find_sample.js
// -----------
// Sample of using of FIND function

// Execute:
//   node.exe find_sample.js
//   VScode -> CTRL f5

const numbers = [3, 15, 24, 6];

// Sample 1 - Using Find function (return first element that evaluates to True)
var newNumbers = numbers.find(function (num) {
  return (num > 10);
});
console.log("Sample 1: " + numbers + " Result: " + newNumbers);

// Sample 2 - Using FindIndex function (return the index of first element that evaluates to True)
var newNumbers = numbers.findIndex(function (num) {
  return (num > 10);
});
console.log("Sample 2: " + numbers + " Result: " + newNumbers);
