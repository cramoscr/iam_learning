import React from "react";

function App() {
  setInterval(showTime, 1000);

  const now = new Date().toLocaleTimeString();

  const [time, getTime] = React.useState(now);

  function showTime() {
    getTime(new Date().toLocaleTimeString());
  }

  return (
    <div className="container">
      <h1>{time}</h1>
      <button onClick={showTime}>Get Time</button>
    </div>
  );
}

export default App;
