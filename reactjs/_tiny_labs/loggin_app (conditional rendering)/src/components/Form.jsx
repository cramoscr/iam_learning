import React from "react";
import Input from "./Input.jsx";
import Button from "./Button.jsx";

function Form(props) {
  return (
    <form className="form">
      <Input type="text" placeholder="Username X" />
      <Input type="password" placeholder="Password X" />
      {props.isRegistered === false && (
        <Input type="password" placeholder="Confirm Password X" />
      )}
      {props.isRegistered ? (
        <Button type="submit" text="Login" />
      ) : (
        <Button type="submit" text="Register" />
      )}
    </form>
  );
}

export default Form;
