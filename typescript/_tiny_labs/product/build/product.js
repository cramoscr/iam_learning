"use strict";
// Typescript Product class sample
// Instructions:
//   Inside /src folder, execute:
//      npm run build
//   This should produce:
//      product.js
class Product {
    name;
    unitPrice;
    constructor(name, unitPrice) {
        this.name = name;
        this.unitPrice = unitPrice;
        this.name = name;
        this.unitPrice = unitPrice;
    }
    getDiscountedPrice(discount) {
        return this.unitPrice - discount;
    }
}
const myJeans = new Product("My jeans", 45);
console.log("Discounted price: " + myJeans.getDiscountedPrice(5));
