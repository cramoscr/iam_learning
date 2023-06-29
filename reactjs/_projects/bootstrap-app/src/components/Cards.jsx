import React from 'react';
import Tab from 'react-bootstrap/Tab';
import Tabs from 'react-bootstrap/Tabs';

import CardsGrid from './Cards_Grid';
import CardsBasic from './Cards_Basic';
import CardsComplex from './Cards_Complex';

function Cards() {
    return (
        <div>
            <h1>This is a Cards example</h1>
            <Tabs defaultActiveKey="basic" id="uncontrolled-tab-example" className="mb-3" >
                <Tab eventKey="basic" title="Basic Card">
                    <h4>Basic Card</h4>
                    <CardsBasic />
                </Tab>
                <Tab eventKey="complex" title="Complex Card">
                    <h4>Complex card</h4>
                    <CardsComplex />
                </Tab>
                <Tab eventKey="grid" title="Cards grid">
                    <h4> Cards Grid</h4>
                    <CardsGrid />                
                </Tab>
            </Tabs>
        </div>
    );
}
export default Cards;