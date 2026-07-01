import type { LoginRequest, LoginResponse } from "../types/auth";

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

export async function loginUser(data: LoginRequest): Promise<LoginResponse> {
  const response = await fetch(`${API_BASE_URL}/api/token/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });

  if (!response.ok) {
    throw new Error("Usuario o contraseña incorrectos");
  }

  return response.json();
}