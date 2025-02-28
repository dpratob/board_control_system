import { useNavigate } from "react-router-dom";

export function BoardCard({ board }) {
  const navigate = useNavigate();

  return (
    <div
      className="bg-zinc-800 p-3 hover:bg-zinc-700 hover:cursor-pointer"
      onClick={() => navigate(`/boards/${board.id}`)}
    >
      <table className="table-auto w-full">
        <tbody>
          <tr>
            <td className="font-bold uppercase">Característica</td>
            <td className="text-slate-400">{board.feature}</td>
          </tr>
          <tr>
            <td className="font-bold uppercase">Grupo</td>
            <td className="text-slate-400">{board.group}</td>
          </tr>
          <tr>
            <td className="font-bold uppercase">Ubicación</td>
            <td className="text-slate-400">{board.location}</td>
          </tr>
          <tr>
            <td className="font-bold uppercase">Sección</td>
            <td className="text-slate-400">{board.section}</td>
          </tr>
          <tr>
            <td className="font-bold uppercase">Número de Serie</td>
            <td className="text-slate-400">{board.serial_number}</td>
          </tr>
          <tr>
            <td className="font-bold uppercase">Estado</td>
            <td className="text-slate-400">
              {board.is_active ? "Activo" : "Inactivo"}
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  );
}