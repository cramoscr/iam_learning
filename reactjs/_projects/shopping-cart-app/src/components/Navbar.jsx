import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav className="bg-blue-600 p-4 text-white flex justify-between">
       <Link to="/" className="font-bold"> Inicio </Link>
       <Link to="/checkout"> Carrito </Link>
    </nav>
  );
}
