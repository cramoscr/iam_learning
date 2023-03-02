import React, { useState } from "react";
import Header from "./Header";
import Footer from "./Footer";
import Note from "./Note";
import CreateArea from "./CreateArea";

import mongoose from "mongoose";

// Connecting to local DB instance
mongoose.connect("mongodb://localhost:27017/keeperDB");

const notesSchema = {
  name: String
}

function App() {
  const [notes, setNotes] = useState([]);


  // This will create the Items collection ( singular name "Item" will be turned into Items collection )
  const Item = mongoose.model("Item", notesSchema);

  function addNote(newNote) {
    setNotes(prevNotes => {
      return [...prevNotes, newNote];
    });
    //Item.insertOne(newNote, function (err) {
    //  if (err) {
    //    console.log("Something goes wrong: " + err);
    //  } else {
    //    console.log("Successfully inserted item into DB...");
    //  }
    //});
  }

  function deleteNote(id) {
    setNotes(prevNotes => {
      return prevNotes.filter((noteItem, index) => {
        return index !== id;
      });
    });
  }

  return (
    <div>
      <Header />
      <CreateArea onAdd={addNote} />
      {notes.map((noteItem, index) => {
        return (
          <Note
            key={index}
            id={index}
            title={noteItem.title}
            content={noteItem.content}
            onDelete={deleteNote}
          />
        );
      })}
      <Footer />
    </div>
  );
}

export default App;
