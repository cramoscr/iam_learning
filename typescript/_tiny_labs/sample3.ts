// Typescript "type annotation" can be used in functions
//  [ getTotal is declared as returning "number" value ]

function getTotal (
    unitPrice: number,
    qty: number,
    discount: number
) : number {
    
    const priceWithoutDiscount = unitPrice * qty;
    const discountAmount = priceWithoutDiscount * discount;

    return priceWithoutDiscount - discount;
}

let test1 = getTotal (10, 5, 0.1);

console.log("test1:" + test1 );

//This should cause an error
let test2: string = getTotal (10, "hola", 0.1);
console.log("test2:" + test2 );
