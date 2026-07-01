import { useState } from "react";
import { useAuth } from "../hooks/useAuth";

export function LoginPage() {
  const { loginMutation } = useAuth();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();

    console.log("CLICK LOGIN");
    console.log("Usuario:", username);
    console.log("Contraseña:", password);

    loginMutation.mutate({
      username,
      password,
    });
  }

  return (
    <div className="login-page">
      <div className="login-card">
        <div className="login-header">
          <div className="login-icon">🦷</div>
          <h1>Clínica Odontológica</h1>
          <p>Sistema de gestión clínica</p>
        </div>

        <form onSubmit={handleSubmit} className="login-form">
          <div className="form-group">
            <label>Usuario</label>
            <input
              type="text"
              value={username}
              onChange={(event) => setUsername(event.target.value)}
              placeholder="Ingrese su usuario"
              required
            />
          </div>

          <div className="form-group">
            <label>Contraseña</label>
            <input
              type="password"
              value={password}
              onChange={(event) => setPassword(event.target.value)}
              placeholder="Ingrese su contraseña"
              required
            />
          </div>

          {loginMutation.isError && (
            <div className="login-error">
              Usuario o contraseña incorrectos.
            </div>
          )}

          <button type="submit" disabled={loginMutation.isPending}>
            {loginMutation.isPending ? "Ingresando..." : "Iniciar sesión"}
          </button>
        </form>
      </div>
    </div>
  );
}