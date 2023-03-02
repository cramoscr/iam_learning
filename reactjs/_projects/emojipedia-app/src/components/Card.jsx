import React from "react";

function Card(props) {
  return (
    <div className="term">
      <dt>
        <span className="emoji" role="img" aria-label="Tense Biceps">
          {props.icon}
        </span>
        <span>{props.title}</span>
      </dt>
      <dd>{props.detail}</dd>
    </div>
  );
}

export default Card;
