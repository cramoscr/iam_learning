// Typescript arrays sample

const numbers: number[] = [];

// Elegant way to force array elements to be "number"
const others: Array<number> = [];

numbers.push(1);

// This must produce an error
numbers.push("two");

// When overing over "morenum" array type is infered
const morenum = [1, 2, 3];

