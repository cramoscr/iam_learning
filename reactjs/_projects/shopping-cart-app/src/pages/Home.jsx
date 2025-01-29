import { useState } from "react";
import ProductCard from "../components/ProductCard";

export default function Home() {
  const [products] = useState([
    { id: 1, name: "Laptop", price: 9999.99, image: "https://via.placeholder.com/150" },
    { id: 2, name: "Mouse", price: 29.99, image: "https://via.placeholder.com/150" },
    { id: 3, name: "Teclado", price: 49.99, image: "https://via.placeholder.com/150" },
  ]);

  const addToCart = (product) => { console.log("Producto agregado:", product); };

  return (
    <div className ="p-5">
       <h1 className="text-2x1 font-bold">Catalogo de Productos</h1>
       <h3> This is the Home page </h3>
       {/*Aqui ira la lista de productos*/}
       <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
         {products.map( (product) => (
            <ProductCard key={product.id} product={product} addtoCart={addToCart} />
         ))}
       </div>
    </div>
  );
}

