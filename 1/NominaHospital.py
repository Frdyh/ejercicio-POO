from typing import List
from Empleado import Empleado


class NominaHospital:
    """
    Servicio de gestión y liquidación de nómina hospitalaria.
    """

    def __init__(self, nombre_hospital: str = "Hospital Universitario Central"):
        self.nombre_hospital = nombre_hospital
        self._empleados: List[Empleado] = []

    def registrar_empleado(self, empleado: Empleado) -> None:
        if not isinstance(empleado, Empleado):
            raise TypeError("El objeto a registrar debe ser una instancia de Empleado.")
        # Evitar duplicados por ID
        if any(e.id_empleado == empleado.id_empleado for e in self._empleados):
            raise ValueError(f"Ya existe un empleado registrado con ID: {empleado.id_empleado}")
        self._empleados.append(empleado)

    @property
    def empleados(self) -> List[Empleado]:
        return list(self._empleados)

    def calcular_total_nomina(self) -> float:
        return sum(emp.calcular_salario_total() for emp in self._empleados)

    def generar_reporte_completo(self) -> str:
        lineas = [
            "=" * 85,
            f"SISTEMA DE NÓMINA - {self.nombre_hospital.upper()}",
            "=" * 85,
        ]
        
        for idx, emp in enumerate(self._empleados, 1):
            desglose = emp.obtener_desglose_nomina()
            lineas.append(f"\n--- Empleado #{idx}: {emp.nombre} ({emp.__class__.__name__}) ---")
            for k, v in desglose.items():
                if "Salario" in k or "Pago" in k or "Bono" in k:
                    if isinstance(v, (int, float)):
                        lineas.append(f"  • {k:<30}: ${v:>12,.2f}")
                    else:
                        lineas.append(f"  • {k:<30}: {str(v):>12}")
                else:
                    lineas.append(f"  • {k:<30}: {str(v):>12}")

        total = self.calcular_total_nomina()
        lineas.append("\n" + "=" * 85)
        lineas.append(f"TOTAL GENERAL DE NÓMINA A PAGAR ({len(self._empleados)} empleados): ${total:,.2f}")
        lineas.append("=" * 85)
        return "\n".join(lineas)
