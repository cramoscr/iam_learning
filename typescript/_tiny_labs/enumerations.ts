// Typescript enumerations

enum Level {
    Low,
    Medium,
    High
}

let my_level = Level.Low;
console.log("my_level: " + my_level);

my_level = Level.High;
console.log("my_level: " + my_level);

//String based enumeration

enum StrLevel {
    Low = "L",
    Medium = "M",
    High = "H"
}

let other_level = StrLevel.High;
console.log("StrLevel: " + StrLevel)

// This should raise an error because "V" is not in the list
other_level = "V";


