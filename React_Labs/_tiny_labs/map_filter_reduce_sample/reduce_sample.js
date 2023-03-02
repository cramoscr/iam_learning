// reduce_sample.js
// -------------
// Sample of using of REDUCE function

// Execute:
//   node.exe reduce_sample.js
//   VScode -> CTRL f5

var numbers = [3, 15, 24, 6];

// Sample 1 - Using Reduce function (in fact it is an accumulator)
var newNumber = numbers.reduce(function (accumulator, currentNumber) {
  console.log("Accumulator: " + accumulator + " CurrentNumber: " + currentNumber);
  return (accumulator + currentNumber);
});
console.log("Sample 1: " + numbers + " Result: " + newNumber);

// Sample 2 -
const array1 = [1, 2, 3, 4];
const initialValue = 0;
const sumWithInitial = array1.reduce(
  (accumulator, currentValue) => accumulator + currentValue,
  initialValue
);
console.log("Sample 2: " + array1 + " Result: " + sumWithInitial);
// expected output: 10