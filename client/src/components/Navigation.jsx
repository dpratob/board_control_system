import { Link } from "react-router-dom";

export function Navigation() {
  return (
    <div className="flex justify-between p-4">
      <Link to="/boards">
        <h1 className="font-bold text-3xl mb-4">Pizarras</h1>
      </Link>
      <button className="bg-indigo-500 px-3 py-2 rounded-lg">
        <Link to="/boards-create">Crear pizarra</Link>
      </button>
    </div>
  );
}