// apps.js
// -------
// Updated: cramos 03/feb/2023
// [ Based on TheLondonAppBrewery ]
// This NodeJS based app handles a ToDo list and stores the data
// into mongoDB database [ called: todolistDB ]
//    (is not using React, just: Express + MongoDB + NodeJS)

// Prerequisits:
//    $ npm install express
//    $ npm install mongoose
//    $ npm install loadash
//    $ npm install ejs

// How to try it:
//   node app.sj

//jshint esversion:6

const express = require("express");
const bodyParser = require("body-parser");
const mongoose = require("mongoose");
const _ = require("lodash");           // <--- Trick here, using "_" as a library name !

const app = express();

app.set('view engine', 'ejs');

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static("public"));

// Connection to Cramos's local PC 
//    {useNewUrlParser} was included only for avoid depecation warning message
//mongoose.connect("mongodb://localhost:27017/todolistDB", { useNewUrlParser: true });

// Connection to Cloud - Atlas based mongoDB
//mongoose.connect("mongodb+srv://user1:txxpxxax@cluster0.bzubbxx.mongodb.net/todolistDB", { useNewUrlParser: true });

const itemsSchema = {
  name: String
}

// This will create the Items collection (note the plural name)
const Item = mongoose.model("Item", itemsSchema);

const items = ["Buy Food", "Cook Food", "Eat Food"];
//const workItems = [];

const item1 = new Item({
  name: "Welcome to the ToDo app"
});

const item2 = new Item({
  name: "Hit the + button to add a new item."
});

const item3 = new Item({
  name: "<--- Hit this to delete an item."
});

const startItems = [item1, item2, item3];

// Defining a two-level structure [ compose structure ]
const listSchema = {
  name: String,
  items: [itemsSchema]
};

const List = mongoose.model("List", listSchema);



/* ---------------- Section Two ----------------- */

// Handling the starting page (showing stored or initial tasks)
app.get("/", function (req, res) {
  //const day = date.getDate();
  Item.find().then((foundItems) => {
    // If ToDo collection is empty, populate it with initial dataset
    if (foundItems.length === 0) {
      Item.insertMany().then((startItems) => {
        // ToDo: work needed here... How to handle errors
          console.log("Successfully inserted starting Items into DB...");
      });
      res.redirect("/");   // <--- Tricky thing ! Reload the page to show default items
    } else {
      // Using "list" component to render the result
      res.render("list", { listTitle: "Today", newListItems: foundItems });
    }
  });
});

// Handling post requests
app.post("/", function (req, res) {
  // list.ejs contains the "newItem" field in the <input> section
  const itemName = req.body.newItem;
  const listName = req.body.list;
  const item = new Item({
    name: itemName
  });
  if (listName === "Today") {
    item.save();
    res.redirect("/");
  } else {
    console.log ('Work needed: app.post ....');
    /*
    List.findOne({ name: listName }, function (err, foundList) {
      foundList.items.push(item);
      foundList.save();
      res.redirect("/" + listName);
    });
    */
  };
});

// Handling deletion
app.post("/delete", function (req, res) {
  const checkedItemId = req.body.checkbox;
  const listName = req.body.listName;

  console.log("listName....................: " + listName);

  if (listName === "Today") {
    Item.findByIdAndRemove().then((checkedItemId) => {
        console.log("Successfully deleted the item !!! ");
        res.redirect("/");
    });
  } else {
    // Something complex is happening here...
    List.findOneAndUpdate({ name: listName }, { $pull: { items: { _id: checkedItemId } } }, function (err, foundItems) {
      if (!err) {
        res.redirect("/" + listName);
      }
    });
  }
});

app.get("/work", function (req, res) {
  res.render("list", { listTitle: "Work List", newListItems: workItems });
});

app.get("/about", function (req, res) {
  res.render("about");
});

// Handling "general" requests [ example: http://localhost:3000/worklist ]
app.get("/:customListName", function (req, res) {
  const customListName = _.capitalize(req.params.customListName);
  console.log('work needed: /customListName...')
  /*
  List.findOne({ name: customListName }, function (err, foundList) {
    if (!err) {
      if (!foundList) {
        // Create a new list
        const list = new List({
          name: customListName,
          items: startItems
        });
        list.save();
        res.redirect("/" + customListName);
      } else {
        // Show existing list items
        res.render("list", { listTitle: foundList.name, newListItems: foundList.items });
      }
    }
    
  }); */
});

// Handling Heroku's dyamic port assignment
let port = process.env.PORT;
if (port == null || port == "") {
  port = 3000;
}

let serverUrl = "http://localhost:" + port;

app.listen(port, function () {
  console.log("Server started successfully.. Try it: " + serverUrl);
});
