import { useEffect, useState } from "react";
import {
  getSpecialists,
  createSpecialist,
  updateSpecialist,
  deleteSpecialist,
} from "../api/specialistApi";
import type { Specialist } from "../types/specialist";
import "../styles/specialist.css";

const emptyForm: Specialist = {
  first_name: "",
  last_name: "",
  specialty: "",
  phone: "",
  email: "",
};

export default function SpecialistsPage() {
  const [specialists, setSpecialists] = useState<Specialist[]>([]);
  const [form, setForm] = useState<Specialist>(emptyForm);
  const [editingId, setEditingId] = useState<number | null>(null);
  const [loading, setLoading] = useState(false);

  async function loadData() {
    setLoading(true);
    try {
      const data = await getSpecialists();
      setSpecialists(data);
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    loadData();
  }, []);

  function handleChange(e: React.ChangeEvent<HTMLInputElement>) {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
  }

  function startEdit(s: Specialist) {
    setForm(s);
    setEditingId(s.id ?? null);
  }

  async function handleSubmit() {
    try {
      if (editingId) {
        await updateSpecialist(editingId, form);
      } else {
        await createSpecialist(form);
      }

      setForm(emptyForm);
      setEditingId(null);
      loadData();
    } catch (error) {
      console.error(error);
    }
  }

  async function handleDelete(id: number) {
    try {
      await deleteSpecialist(id);
      loadData();
    } catch (error) {
      console.error(error);
    }
  }

  return (
    <div className="container">
      <h2 className="title">Sistema de Gestión Clínica</h2>
      <h3 className="subtitle">Especialistas</h3>

      <div className="card">
        <input
          className="input"
          name="first_name"
          placeholder="Nombre"
          value={form.first_name}
          onChange={handleChange}
        />

        <input
          className="input"
          name="last_name"
          placeholder="Apellido"
          value={form.last_name}
          onChange={handleChange}
        />

        <input
          className="input"
          name="specialty"
          placeholder="Especialidad"
          value={form.specialty}
          onChange={handleChange}
        />

        <input
          className="input"
          name="phone"
          placeholder="Teléfono"
          value={form.phone}
          onChange={handleChange}
        />

        <input
          className="input"
          name="email"
          placeholder="Email"
          value={form.email}
          onChange={handleChange}
        />

        <button className="button button-primary" onClick={handleSubmit}>
          {editingId ? "Actualizar" : "Crear"}
        </button>

        <button
          className="button"
          onClick={() => {
            setForm(emptyForm);
            setEditingId(null);
          }}
        >
          Limpiar
        </button>
      </div>

      {loading && <p>Cargando...</p>}

      <table className="table">
        <thead>
          <tr>
            <th>Nombre</th>
            <th>Apellido</th>
            <th>Especialidad</th>
            <th>Teléfono</th>
            <th>Email</th>
            <th>Acciones</th>
          </tr>
        </thead>

        <tbody>
          {specialists.map((s) => (
            <tr key={s.id}>
              <td>{s.first_name}</td>
              <td>{s.last_name}</td>
              <td>{s.specialty}</td>
              <td>{s.phone}</td>
              <td>{s.email}</td>
              <td>
                <button
                  className="button button-edit"
                  onClick={() => startEdit(s)}
                >
                  Editar
                </button>

                <button
                  className="button button-delete"
                  onClick={() => handleDelete(s.id!)}
                >
                  Eliminar
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}