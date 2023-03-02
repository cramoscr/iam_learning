import React from "react";

function Button(props) {
  return (
    <button style={{ backgroundColor: "red" }} onClick={handleClick}>
      Submit
    </button>
  );
}

export default Button;
