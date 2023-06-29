import './App.css';

import Home          from './components/Home';
import Cards         from './components/Cards';

import About         from './components/About';
import Contact       from './components/Contact';
import NavigationBar from './components/NavigationBar';
import NavBar        from './components/Navbar';

import 'react-bootstrap/dist/react-bootstrap.min.js';
//import { BrowserRouter as Router, Route } from 'react-router-dom';
import { BrowserRouter, Routes, Route } from "react-router-dom";

function App() {
   return (
     <div className="App">
        <BrowserRouter>
            <NavigationBar />
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/Cards" element={<Cards />} />
                <Route path="/About" element={<About />} />
                <Route path="/Contact" element={<Contact />} />
            </Routes>
        </BrowserRouter>
     </div>
   );
}
export default App;