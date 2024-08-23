// Typescript object aliases sample

type Product_x = { name: string; unitPrice?: number};

let table: Product = { 
    name: "Table",
    purchase: (qty) => 
        console.log('Purchased ${qty} tables'),
 };
 table.purchase(4);

let chair: Product_x = { name: "Chair", unitPrice: 40};

// "intersection type" sample
type DiscountedProduct = Product_x & { discount: number };

let chairOnSale: DiscountedProduct = {
    name: "Chair on sale",
    unitPrice: 30,
    discount: 0.5,
}

// Type representing a function
type Purchase = (qty: number) => void;
type Product = {
    name: string;
    unitPrice?: number;
    purchase: Purchase;
}
