import type { Patient } from "../types/patient";

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

export async function getPatients(): Promise<Patient[]> {
  const token = localStorage.getItem("access_token");

  const response = await fetch(`${API_BASE_URL}/api/patients/`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  if (!response.ok) {
    throw new Error("Error al obtener pacientes");
  }

  return response.json();
}