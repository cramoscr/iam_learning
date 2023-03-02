// app.js
// -------
// Updated: cramos 27/jan/2023
//
// This app shows how to perform CRUD operations using Mongoose library
//
// Tricky:
//    Note that code doesn't execute top/down 
//    ( last line is printed before cars enumeration)

// ToDo:
//   I still need to learn how to warranty the correct (cronological | logical) order
//   of UPDATE / DELETE commands ( currently, it happens unordered | uncontrolled | bad way)

const mongoose = require ('mongoose');

// This supress a warning message
mongoose.set('strictQuery', true);

// carsDB will be created if not exists
mongoose.connect("mongodb://localhost:27017/carsDB");

// Create the schema for Car instances
//   Tip: doors field includes validation rules !
const carSchema = new mongoose.Schema ({
    _id: Number,
    brand: String,
    model: String,
    doors: {
        type: Number,
        min: 1,
        max: 5
    }
});

// Defines the Car class structure. 
//   Tip: mongoDB will turn "Car" into "cars" [lowercase, plural] collection
const myCar = mongoose.model("Car", carSchema);

// Creation of the new instance ("record")
const carObj = new myCar ({
    _id: 1,
    brand: "LandRover",
    model: "Discovery",
    doors: 5
});

// Creates the DB (if doesn't exist), the Collection (if doesn't exists) and
// inserts the instance ("record")
carObj.save();

// Now, inserting several recors at once
const tesla  = new myCar({_id:2, brand:"Tesla", model:"Model-S", doors: 4});
const camaro = new myCar({_id:3, brand:"Chevrolet", model:"Camaro", doors: 2});
const montero = new myCar({_id:4, brand:"Mitsubishi", model:"Montero", doors: 5});
const discovery = new myCar({_id:5, brand:"LandRover", model:"Defender", doors: 5});

myCar.insertMany( [tesla, camaro, montero, discovery], function (err) {
    if (err) {
        console.log(err);
    } else {
        console.log("Successfully saved all cars to CarsDB");
    }
});

// Updating single record
myCar.updateOne({_id: 1},{model: "Discovery 5-XL"}, function(err){
    if (err) {
        console.log("Update failed..." + err);
    } else {
        console.log("Successfully updated the Car info");
    }
});

// Deleting single record
myCar.deleteOne({brand: "LandRover"}, function(err){
    if (err) {
        console.log("Deletion failed..." + err);
    } else {
        console.log("Successfully DELETE the Car record");
    }
});

// Using the Find() function for Cars enumeration
myCar.find(function(err, carArray){
    if (err) {
        console.log(err);
    } else {
        // Printing the collection contents
        carArray.forEach(function(carElement){
            console.log("Car brand: " + carElement.brand);
        });
    }
});

// Extending an Schema

// ToDo: Learn where/how to handle the DB connection closing process
// mongoose.connection.close();

// To check results: 
//    - enter into mongoSH
//    - enter show databases, show collections, etc
//    - enter use carsDB
//    - enter db.cars.find()

console.log("Cars App finished....");