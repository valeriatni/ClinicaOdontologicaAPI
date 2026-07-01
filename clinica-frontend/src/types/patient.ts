export interface Patient {
  id: number;
  first_name: string;
  last_name: string;
  dni: string;
  phone: string | null;
  email: string | null;
  birth_date: string | null;
  address: string | null;
  is_active: boolean;
}