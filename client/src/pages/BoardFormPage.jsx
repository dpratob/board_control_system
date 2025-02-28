import { useEffect } from "react";
import { useForm } from "react-hook-form";
import { useNavigate, useParams } from "react-router-dom";
import {
  createBoard,
  deleteBoard,
  updateBoard,
  getBoard,
} from "../api/boards.api";
import { toast } from "react-hot-toast";

export function BoardFormPage() {
  const {
    register,
    handleSubmit,
    formState: { errors },
    setValue,
  } = useForm();
  const navigate = useNavigate();
  const params = useParams();

  useEffect(() => {
    async function loadBoard() {
      if (params.id) {
        const { data } = await getBoard(params.id);
        setValue("feature", data.feature);
        setValue("group", data.group);
        setValue("location", data.location);
        setValue("section", data.section);
        setValue("serial_number", data.serial_number);
        setValue("is_active", data.is_active);
      }
    }
    loadBoard();
  }, [params.id, setValue]);

  const onSubmit = handleSubmit(async (data) => {
    if (params.id) {
      await updateBoard(params.id, data);
    } else {
      await createBoard(data);
      toast.success("Board created", {
        position: "bottom-right",
        style: {
          background: "#101010",
          color: "#fff",
        },
      });
    }
    navigate("/boards");
  });

  return (
    <div className="max-w-x1 mx-auto">
      <form onSubmit={onSubmit}>
        <input
          type="text"
          placeholder="Característica"
          {...register("feature", { required: true })}
          className="bg-zinc-700 p-3 rounded-lg block w-full mb-3"
        />
        {errors.feature && <span>La característica es obligatoria</span>}

        <input
          type="text"
          placeholder="Grupo"
          {...register("group", { required: true })}
          className="bg-zinc-700 p-3 rounded-lg block w-full mb-3"
        />
        {errors.group && <span>El grupo es obligatorio</span>}

        <input
          type="text"
          placeholder="Ubicación"
          {...register("location", { required: true })}
          className="bg-zinc-700 p-3 rounded-lg block w-full mb-3"
        />
        {errors.location && <span>La ubicación es obligatoria</span>}

        <input
          type="text"
          placeholder="Sección"
          {...register("section", { required: true })}
          className="bg-zinc-700 p-3 rounded-lg block w-full mb-3"
        />
        {errors.section && <span>La sección es obligatoria</span>}

        <input
          type="text"
          placeholder="Número de serie"
          {...register("serial_number", { required: true })}
          className="bg-zinc-700 p-3 rounded-lg block w-full mb-3"
        />
        {errors.serial_number && <span>El número de serie es obligatorio</span>}

        <input
          type="checkbox"
          id="isActive"
          {...register("is_active")}
          className="bg-zinc-700 p-3 rounded-lg block w-fill mb-3"
        />
        <label htmlFor="isActive">¿Está activo?</label>
        {errors.is_active && <span>El estado es obligatorio</span>}

        <button className="bg-indigo-500 p-3 rounded-lg block w-full mt-3">
          Guardar
        </button>
      </form>

      {params.id && (
        <div className="flex justify-end">
          <button
            className="bg-red-500 p-3 rounded-lg w-48 mt-3"
            onClick={async () => {
              const accepted = window.confirm("¿Estás seguro?");
              if (accepted) {
                await deleteBoard(params.id);
                toast.success("Tablero eliminado", {
                  position: "bottom-right",
                  style: {
                    background: "#101010",
                    color: "#fff",
                  },
                });
                navigate("/boards");
              }
            }}
          >
            Eliminar
          </button>
        </div>
      )}
    </div>
  );
}