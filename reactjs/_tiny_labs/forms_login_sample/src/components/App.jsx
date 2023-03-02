import React, { useState } from "react";

function App() {
  const [name, setName] = useState("");
  const [headingText, setHeading] = useState("");
  const [isMouseOver, setMouseOver] = useState(false);

  function handleMouseOver() {
    setMouseOver(true);
  }
  function handleMouseOut() {
    setMouseOver(false);
  }

  function handleChange(event) {
    console.log("value: " + event.target.value);
    console.log("placeholder: " + event.target.placeholder);
    console.log("type: " + event.target.type);
    setName(event.target.value);
  }

  function handleClick(event) {
    setHeading(name);
    // This avoid default reloading after submit button pressed
    event.preventDefault();
  }

  return (
    <div className="container">
      <h1>Hello, {headingText} </h1>
      <form onSubmit={handleClick}>
        <input
          onChange={handleChange}
          type="text"
          placeholder="What's your name?"
          value={name}
        />
        <button
          type="submit"
          style={{ backgroundColor: isMouseOver ? "black" : "white" }}
          onMouseOver={handleMouseOver}
          onMouseOut={handleMouseOut}
        >
          Submit
        </button>
      </form>
    </div>
  );
}

export default App;
