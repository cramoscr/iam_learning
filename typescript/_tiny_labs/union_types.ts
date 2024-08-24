// Typescript union type sample

type Level = "H" | "M" | "L";

type RGB = "red" | "green" | "blue";

let color: RGB = "red";
console.log("color: " + color);

// This should raise an error because "gray" is not in the RGB list
color = "gray";
