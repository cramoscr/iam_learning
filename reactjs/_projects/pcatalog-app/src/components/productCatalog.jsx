import React from "react";
import logo from '../assets/ferrari.jpg';

function ProductCatalog() {
  return (
    renderTile = () => {
        return <ProductTile></ProductTile>;
    }

    render() {
        let tiles = [];
        for (let i = 0; i < 8; i++) {
            tiles.push(this.renderTile());
        }
        return tiles;
    }
 );
}

export default ProductCatalog;
