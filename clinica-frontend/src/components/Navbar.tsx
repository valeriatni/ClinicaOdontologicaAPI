import { useNavigate } from "react-router-dom";
import { useAuthContext } from "../context/authContext";

export function Navbar() {
  const navigate = useNavigate();
  const { logout } = useAuthContext();

  function handleLogout() {
    logout();
    navigate("/login");
  }

  return (
    <header className="topbar">
      <div>
        <h1>Sistema de Gestión Clínica</h1>
        <p>Panel administrativo de la clínica odontológica</p>
      </div>

      <div className="user-box">
        <span>Administrador</span>
        <button className="logout-button" onClick={handleLogout}>
          Salir
        </button>
      </div>
    </header>
  );
}