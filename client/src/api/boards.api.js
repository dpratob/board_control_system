import axios from "axios";

const boardsApi = axios.create({
  baseURL: "http://127.0.0.1:8000/board/board/",
});

export const getAllBoards = () => boardsApi.get("/");
export const getBoard = (id) => boardsApi.get(`/${id}/`);
export const createBoard = (board) => boardsApi.post("/", board);
export const deleteBoard = (id) => boardsApi.delete(`/${id}/`);
export const updateBoard = (id, board) => boardsApi.put(`/${id}/`, board);