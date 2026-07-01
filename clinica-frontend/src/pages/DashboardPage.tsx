import { useDashboard } from "../hooks/useDashboard";
import { StatCard } from "../components/StatCard";

export function DashboardPage() {
  const { data, isLoading, isError } = useDashboard();

  if (isLoading) {
    return <p>Cargando dashboard...</p>;
  }

  if (isError) {
    return <p>Error al cargar el dashboard.</p>;
  }

  return (
    <div>
      <h2 className="page-title">Dashboard</h2>

      <div className="stats-grid">
        <StatCard
          title="Pacientes registrados"
          value={data?.patients}
          description="Pacientes activos en la clínica"
        />

        <StatCard
          title="Especialistas"
          value={data?.specialists}
          description="Profesionales disponibles"
        />

        <StatCard
          title="Citas registradas"
          value={data?.appointments}
          description="Citas no canceladas"
        />

        <StatCard
          title="Historias clínicas"
          value={data?.medical_records}
          description="Registros clínicos activos"
        />

        <StatCard
          title="Presupuestos"
          value={data?.budgets}
          description="Presupuestos no rechazados"
        />

        <StatCard
          title="Pagos"
          value={data?.payments}
          description="Pagos registrados"
        />
      </div>
    </div>
  );
}