import { useState } from "react";
import { usePatients } from "../hooks/usePatients";
import { PatientModal } from "../components/patientModal";

export function PatientsPage() {
  const { data, isLoading, isError } = usePatients();
  const [search, setSearch] = useState("");
  const [isModalOpen, setIsModalOpen] = useState(false);

  const filteredPatients = data?.filter((patient) => {
    const fullName = `${patient.first_name} ${patient.last_name}`.toLowerCase();

    return (
      fullName.includes(search.toLowerCase()) ||
      patient.dni.includes(search) ||
      patient.email?.toLowerCase().includes(search.toLowerCase())
    );
  });

  if (isLoading) {
    return <p>Cargando pacientes...</p>;
  }

  if (isError) {
    return <p>Error al cargar pacientes.</p>;
  }

  return (
    <div>
      <div className="page-header">
        <div>
          <h2 className="page-title">Pacientes</h2>
          <p>Gestión de pacientes registrados en la clínica.</p>
        </div>

        <button
          className="btn btn-primary"
          onClick={() => setIsModalOpen(true)}
        >
          + Nuevo paciente
        </button>
      </div>

      <div className="search-box">
        <input
          type="text"
          placeholder="Buscar por nombre, DNI o correo..."
          value={search}
          onChange={(event) => setSearch(event.target.value)}
        />
      </div>

      <div className="table-card">
        <table className="table table-hover align-middle">
          <thead>
            <tr>
              <th>DNI</th>
              <th>Paciente</th>
              <th>Teléfono</th>
              <th>Correo</th>
              <th>Estado</th>
              <th>Acciones</th>
            </tr>
          </thead>

          <tbody>
            {filteredPatients?.map((patient) => (
              <tr key={patient.id}>
                <td>{patient.dni}</td>
                <td>
                  {patient.first_name} {patient.last_name}
                </td>
                <td>{patient.phone ?? "Sin teléfono"}</td>
                <td>{patient.email ?? "Sin correo"}</td>
                <td>
                  <span
                    className={
                      patient.is_active
                        ? "badge bg-success"
                        : "badge bg-secondary"
                    }
                  >
                    {patient.is_active ? "Activo" : "Inactivo"}
                  </span>
                </td>
                <td>
                  <button className="btn btn-sm btn-outline-primary me-2">
                    Editar
                  </button>

                  <button
                    className={
                      patient.is_active
                        ? "btn btn-sm btn-outline-danger"
                        : "btn btn-sm btn-outline-success"
                    }
                  >
                    {patient.is_active ? "Desactivar" : "Activar"}
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>

        {filteredPatients?.length === 0 && (
          <p className="empty-message">No se encontraron pacientes.</p>
        )}
      </div>

      <PatientModal
        isOpen={isModalOpen}
        onClose={() => setIsModalOpen(false)}
      />
    </div>
  );
}