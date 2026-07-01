import { NavLink } from "react-router-dom";

export function Sidebar() {
  return (
    <aside className="sidebar">
      <div className="sidebar-brand">
        <span className="brand-icon">🦷</span>
        <div>
          <h2>Clínica</h2>
          <p>Odontológica</p>
        </div>
      </div>

      <nav className="sidebar-nav">
        <NavLink to="/dashboard">Dashboard</NavLink>
        <NavLink to="/patients">Pacientes</NavLink>
        <NavLink to="/specialists">Especialistas</NavLink>
        <NavLink to="/appointments">Citas</NavLink>
      </nav>
    </aside>
  );
}