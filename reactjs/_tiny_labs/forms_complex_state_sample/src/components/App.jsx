import React, { useState } from "react";

function App() {
  const [contact, setContact] = useState({
    fName: "",
    lName: "",
    email: ""
  });

  function handleChange(event) {
    // This is called JS "destructuring" (produce a "plain" datastructure)
    const { name, value } = event.target;

    // Highly elevated science here !!!
    setContact((prevValue) => {
      if (name === "fName") {
        return {
          fName: value,
          lName: prevValue.lName,
          email: prevValue.email
        };
      } else if (name === "lName") {
        return {
          fName: prevValue.fName,
          lName: value,
          email: prevValue.email
        };
      } else if (name === "email") {
        return {
          fName: prevValue.fName,
          lName: prevValue.lName,
          email: value
        };
      }
    });
  }

  function handleClick(event) {
    console.log("clicked");
    event.preventDefault();
  }

  return (
    <div className="container">
      <h1>
        Hello {contact.fName} {contact.lName}
      </h1>
      <p>{contact.email}</p>
      <form onSubmit={handleClick}>
        <input
          name="fName"
          value={contact.fName}
          onChange={handleChange}
          placeholder="First Name"
        />
        <input
          name="lName"
          value={contact.lName}
          onChange={handleChange}
          placeholder="Last Name"
        />
        <input
          name="email"
          value={contact.email}
          onChange={handleChange}
          placeholder="Email"
        />
        <button>Submit</button>
      </form>
    </div>
  );
}

export default App;
