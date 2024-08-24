// Typescript Product class sample

// Instructions:
//   Inside /src folder, execute:
//      npm run build
//   This should produce:
//      product.js

class Product {
    constructor(public name: string, public unitPrice: number) {
        this.name = name;
        this.unitPrice = unitPrice;
    }
    getDiscountedPrice(discount: number): number {
        return this.unitPrice - discount;
    }
}

const myJeans = new Product ("My jeans", 45);
console.log("Discounted price: " + myJeans.getDiscountedPrice(5));
