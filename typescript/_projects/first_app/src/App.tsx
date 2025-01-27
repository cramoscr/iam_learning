import React from 'react';
import logo from './logo.svg';
import './App.css';
import { Alert } from './Alert';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <span>
          This is my first "create-react-app" lab...
          <br />
          And is looking really good !
        </span>
        <p>
          Edit <code>src/App.tsx</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <div>
          <Alert heading="Success" closable>
            Everything is really good!
          </Alert>
        </div>
      </header>
    </div>
  );
}
export default App;
