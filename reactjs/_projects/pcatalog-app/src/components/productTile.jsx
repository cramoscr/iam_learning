import React from "react";
import logo from '../assets/ferrari.jpg';

function ProductTile() {
  return (
    <div class="card">
        <div class="card-image">
            <figure class="image is-4by3">
                <img src={logo} alt="Ferrari icon"></img>
            </figure>
        </div>
        <div class="card-content">
            <p class="title product-title">This is a Ferrari</p>

            <div class="content">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus nec iaculis mauris.
                <br></br>
            </div>
            <a class="button is-primary" href="product.html" target="_blank">
                <strong>More Details</strong>
            </a>
        </div>
    </div>
 );
}

export default ProductTile;
