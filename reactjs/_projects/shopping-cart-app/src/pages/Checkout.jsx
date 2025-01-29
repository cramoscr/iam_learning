import { useCart } from "../context/CartContext";

export default function Checkout() {
  const { cart, removeFromCart, clearCart } = useCart();

  return (
    <div className="p-5">
      <h1 className="text-2xl font-bold mb-4">Carrito de Compras</h1>
      {cart.length === 0 ? (
        <p>El carrito está vacío.</p>
      ) : (
        <div className="space-y-4">
          {cart.map((item) => (
            <div key={item.id} className="border p-4 rounded-md shadow-md flex justify-between items-center">
              <div>
                <h2 className="font-bold">{item.name}</h2>
                <p>${item.price.toFixed(2)} x {item.quantity}</p>
              </div>
              <button 
                onClick={() => removeFromCart(item.id)}
                className="bg-red-500 text-white px-3 py-1 rounded hover:bg-red-600"
              >
                Eliminar
              </button>
            </div>
          ))}
          <button 
            onClick={clearCart}
            className="bg-gray-700 text-white px-4 py-2 rounded hover:bg-gray-800 mt-4"
          >
            Vaciar Carrito
          </button>
        </div>
      )}
    </div>
  );
}
