// mongoose_connect.js
// ----------------
// Updated: cramos 27/jan/2023
//
// This code shows how to connect to mongoDB [ carsDB ] using
// the monGOOSE library
//
// Tricky:
//    Note that code doesn't execute top/down 
//    ( last line is printed before cars enumeration)

const mongoose = require ('mongoose');

// This will supress a warning message
mongoose.set('strictQuery', true);

// carsDB will be created if doesn't exists
//mongoose.connect("mongodb://localhost:27017/carsDB");

// Connection to Cloud - Atlas based mongoDB
mongoose.connect("mongodb+srv://user1:temporal@cluster0.bzubbxx.mongodb.net/carsDB", { useNewUrlParser: true });

// Create the schema for Car instances
const carSchema = new mongoose.Schema ({
    brand: String,
    model: String,
    doors: Number,
});

// defines the Car class structure. 
// Tip: mongoDB will turn "Car" into "cars" [lowercase, plural] collection
const myCar = mongoose.model("Car", carSchema);

// Creation of the new instance ("record")
const carObj = new myCar ({
    brand: "Landrover",
    model: "Discovery",
    doors: 5
});

// Creates the DB and Collection (if didn't exists) and inserts the instance ("record")
carObj.save();

console.log("Cars App finished....");
