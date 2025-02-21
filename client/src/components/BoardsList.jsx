import { useEffect, useState } from "react";
import { getAllBoards } from "../api/boards.api";
import { BoardCard } from "./BoardCard";

export function BoardsList() {
  const [boards, setBoards] = useState([]);

  useEffect(() => {
    async function loadBoards() {
      const res = await getAllBoards();
      setBoards(res.data);
    }
    loadBoards();
  }, []);

  return (
    <div className="grid grid-cols-3 gap-3">
      {boards.map((board) => (
        <BoardCard key={board.id} board={board} />
      ))}
    </div>
  );
}