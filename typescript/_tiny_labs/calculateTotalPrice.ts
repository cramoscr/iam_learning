// Using the Typescript "type notation" feature allows the
// editor to highlight programming errors
//  [ product.price is incorrect ! 
//      should be product.unitPrice ]

function calculateTotalPrice(
    product: { name:string; unitPrice: number},
    quantity: number,
    discount: number
) {
    const priceWithoutDiscount = product.price * quantity;
    const discountAmount = priceWithoutDiscount * discount;
    return priceWithoutDiscount - discountAmount;
}