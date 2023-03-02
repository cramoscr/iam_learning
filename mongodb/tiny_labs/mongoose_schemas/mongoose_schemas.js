// mongoose_schemas.js
// ----------------
// Updated: cramos 30/jan/2023
//
// This app shows how to combile several schemas into a single collection

const mongoose = require ('mongoose');

// This supress a warning message
mongoose.set('strictQuery', true);

// carsDB will be created if not exists
mongoose.connect("mongodb://localhost:27017/carsDB");

// Defines the schema for Engine instances
const engineSchema = new mongoose.Schema ({
    _id: Number,
    fuel: String,
    transmission: String,
    power: String, 
    cylinders: Number
});

// Defines the schema for Car instances
//   Tip: doors field includes validation rules !
const carSchema = new mongoose.Schema ({
    _id: Number,
    brand: String,
    model: String,
    doors: {
        type: Number,
        min: 1,
        max: 5
    },
    engine: engineSchema
});

// Defines the Car class structure. 
//   Tip: mongoDB will turn "Car" into "cars" [lowercase, plural] collection
const Car = mongoose.model("Car", carSchema);

// Defines the Engine class structure. 
const Engine = mongoose.model("Engine", engineSchema);

// Definition of new Engine instances
const dieselEngine = new Engine({
    _id: 1,
    fuel: "Diesel",
    transmission: "Automatic",
    power: "3000 CC",
    cylinders: 4
});
const gasolineEngine = new Engine({
    _id: 2,
    fuel: "Gasoline",
    transmission: "Manual",
    power: "1600 CC",
    cylinders: 4
});
dieselEngine.save();
gasolineEngine.save();

// Creation of the new Car instance ("record")
const carObj = new Car ({
    _id: 10,
    brand: "Fiat",
    model: "Fiesta",
    doors: 5,
    engine: gasolineEngine,
});

// Creates the DB (if doesn't exist), the Collection (if doesn't exists) and
// inserts the instance ("record")
carObj.save();

// ToDo: Learn where/how to handle the DB connection closing process
// mongoose.connection.close();

// To check results: 
//    - enter into mongoSH
//    - enter show databases, show collections, etc
//    - enter use carsDB
//    - enter db.cars.find()

console.log("Mongoose_Schemas App finished....");