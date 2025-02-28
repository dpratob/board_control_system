import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { BoardsPage } from "./pages/BoardsPage";
import { BoardFormPage } from "./pages/BoardFormPage";
import { BoardFeaturesPage } from "./pages/BoardFeaturesPage";
import { Navigation } from "./components/Navigation";
import { Toaster } from "react-hot-toast";

function App() {
  return (
    <BrowserRouter>
      <div className="container mx-auto">
        <Navigation />
        <Routes>
          <Route path="/" element={<Navigate to="/boards" />} />
          <Route path="/boards" element={<BoardsPage />} />
          <Route path="/boards-create" element={<BoardFormPage />} />
          <Route path="/boards/:id" element={<BoardFormPage />} />
        </Routes>
        <Toaster />
      </div>
    </BrowserRouter>
  );
}

export default App;