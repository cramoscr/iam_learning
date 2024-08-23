// Typescript object type sample

let table = { name: "Table", unitPrice: 450};

// This should raise error "discount does not exist"
table.discount = 10;

// Question mark: "?" makes an argument optional
const table2: { name: string; unitPrice?: number } = {
    name: "Table2",
};
