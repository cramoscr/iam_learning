// Typescript class sample

// This way, "any" type is inferred for name and unitPrice
class Product_x {
    name;
    unitPrice;
}

class Product {
    name: string;
    unitPrice: number;
}

// Making attributes optional
class Product_z {
    name?: string;
    unitPrice?: number;
}

//Using "constructor" clause (format 1)
class Product_w {
    name;
    unitPrice;
    constructor (name: string, unitPrice: number) {
        this.name = name;
        this.unitPrice = unitPrice;
    }
}

//Using "constructor" clause (format 2)
class Product_y {
    constructor(public name: string, public unitPrice: number) {
        this.name = name;
        this.unitPrice = unitPrice;
    }
}

class Product_b {
    constructor(public name: string, public unitPrice: number){
        this.name = name;
        this.unitPrice = unitPrice
    }
    getDiscountedPrice(discount: number): number {
        return this.unitPrice - discount;
    }
}

// Using classes
const table = new Product_b("My table", 45);
console.log(table.getDiscountedPrice(5));

