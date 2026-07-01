import { useQuery } from "@tanstack/react-query";
import { getPatients } from "../api/patientApi";

export function usePatients() {
  return useQuery({
    queryKey: ["patients"],
    queryFn: getPatients,
  });
}