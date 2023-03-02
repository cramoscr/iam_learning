// arrow_functions_sample.js
// ----------------------
// Sample of using of ARROW function syntax

// Execute:
//   node.exe arrow_functions_sample.js
//   VScode -> CTRL f5

var numbers = [3, 15, 24, 6];

// Sample 1 - Using MAP function with standard syntax
var newNumbers = numbers.map(function double(x) {
  return x * 2;
});
console.log("Sample 1: " + numbers + " Result: " + newNumbers);

// Sample 2 - Using MAP function with Arrow syntax
var newNumbers = numbers.map( x => {
  return x * 2;
});
console.log("Sample 2: " + numbers + " Result: " + newNumbers);

// Sample 3 - Using MAP function with Arrow syntax (shorter format)
var newNumbers = numbers.map( x => x * 2);
console.log("Sample 3: " + numbers + " Result: " + newNumbers);

