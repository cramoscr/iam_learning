// Typescript interface sample

interface Product_x { name: string; unitPrice?: number};

let table: Product = { 
    name: "Table",
    purchase: (qty) => 
        console.log('Purchased ${qty} tables'),
 };
 table.purchase(4);

let chair: Product_x = { name: "Chair", unitPrice: 40};

// "intersection type" sample
interface DiscountedProduct extends Product_x { discount: number };

let chairOnSale: DiscountedProduct = {
    name: "Chair on sale",
    unitPrice: 30,
    discount: 0.5,
}

// Type representing a function
interface Purchase { (qty: number) : void };

interface Product {
    name: string;
    unitPrice?: number;
    purchase: Purchase;
}
