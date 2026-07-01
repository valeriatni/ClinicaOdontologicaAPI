import type { Specialist } from "../types/specialist";

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

// LISTAR
export async function getSpecialists(): Promise<Specialist[]> {
  const token = localStorage.getItem("access_token");

  const response = await fetch(`${API_BASE_URL}/api/specialists/`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  if (!response.ok) {
    throw new Error("Error al obtener especialistas");
  }

  return response.json();
}

// CREAR
export async function createSpecialist(data: Specialist) {
  const token = localStorage.getItem("access_token");

  const response = await fetch(`${API_BASE_URL}/api/specialists/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
    body: JSON.stringify(data),
  });

  if (!response.ok) {
    throw new Error("Error al crear especialista");
  }

  return response.json();
}

// EDITAR
export async function updateSpecialist(id: number, data: Specialist) {
  const token = localStorage.getItem("access_token");

  const response = await fetch(`${API_BASE_URL}/api/specialists/${id}/`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
    body: JSON.stringify(data),
  });

  if (!response.ok) {
    throw new Error("Error al actualizar especialista");
  }

  return response.json();
}

// ELIMINAR
export async function deleteSpecialist(id: number) {
  const token = localStorage.getItem("access_token");

  const response = await fetch(`${API_BASE_URL}/api/specialists/${id}/`, {
    method: "DELETE",
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  if (!response.ok) {
    throw new Error("Error al eliminar especialista");
  }
}