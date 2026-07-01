import { useMutation } from "@tanstack/react-query";
import { useNavigate } from "react-router-dom";
import { loginUser } from "../api/authApi";
import type { LoginRequest } from "../types/auth";
import { useAuthContext } from "../context/authContext";

export function useAuth() {
  const navigate = useNavigate();
  const { login } = useAuthContext();

  const loginMutation = useMutation({
    mutationFn: (data: LoginRequest) => loginUser(data),
    onSuccess: (data) => {
      login(data.access, data.refresh);
      navigate("/dashboard");
    },
  });

  return {
    loginMutation,
  };
}