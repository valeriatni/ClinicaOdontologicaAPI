interface PatientModalProps {
  isOpen: boolean;
  onClose: () => void;
}

export function PatientModal({ isOpen, onClose }: PatientModalProps) {
  if (!isOpen) {
    return null;
  }

  return (
    <div className="modal-backdrop-custom">
      <div className="modal-card">
        <div className="modal-header-custom">
          <h3>Registrar paciente</h3>
          <button onClick={onClose}>×</button>
        </div>

        <form className="patient-form">
          <div className="form-row">
            <div className="form-group">
              <label>Nombres</label>
              <input type="text" placeholder="Ej. Juan" />
            </div>

            <div className="form-group">
              <label>Apellidos</label>
              <input type="text" placeholder="Ej. Pérez" />
            </div>
          </div>

          <div className="form-row">
            <div className="form-group">
              <label>DNI</label>
              <input type="text" placeholder="8 dígitos" />
            </div>

            <div className="form-group">
              <label>Teléfono</label>
              <input type="text" placeholder="Ej. 987654321" />
            </div>
          </div>

          <div className="form-group">
            <label>Correo</label>
            <input type="email" placeholder="correo@ejemplo.com" />
          </div>

          <div className="form-group">
            <label>Fecha de nacimiento</label>
            <input type="date" />
          </div>

          <div className="form-group">
            <label>Dirección</label>
            <textarea placeholder="Dirección del paciente" />
          </div>

          <div className="modal-actions">
            <button type="button" className="btn btn-secondary" onClick={onClose}>
              Cancelar
            </button>

            <button type="button" className="btn btn-primary">
              Guardar paciente
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}