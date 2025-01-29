export default function ProductCard({ product, addToCart }) {
  return (
    <div className="border rounded-lg p-4 shadow-md">
       <img src={product.image} alt={product.name} className="w-full h40 object-cover rounded-md" />
       <h2 className="text-lg font-bold mt-2">{product.name}</h2>
       <p className="text-gray-700">${product.price.toFixed(2)}</p>
       <button 
          onClick={() => addToCart(product)}
          className="bg-blue-600 text-white px-4 py-2 mt-2 rounded hover:bg-blue-700" >
          Agregar al Carrito
       </button>
    </div>       
  );
}
