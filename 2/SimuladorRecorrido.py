from typing import List, Tuple
from Vehiculo import Vehiculo
from VehiculoAnfibio import VehiculoAnfibio


class SimuladorRecorrido:

    def __init__(self):
        self._tramos: List[Tuple[str, float]] = []  # (medio, distancia_km)

    def agregar_tramo(self, medio: str, distancia_km: float) -> None:
        if distancia_km <= 0:
            raise ValueError("La distancia del tramo debe ser positiva.")
        self._tramos.append((medio.lower(), distancia_km))

    def ejecutar_simulacion_anfibio(self, anfibio: VehiculoAnfibio) -> str:
        lineas = [
            "=" * 85,
            f"SIMULACIÓN DE RECORRIDO MULTI-TRAMO PARA: {anfibio.nombre.upper()}",
            "=" * 85,
        ]

        consumo_inicial = anfibio.combustible_consumido_total
        consumo_acumulado_viaje = 0.0

        for i, (medio_tramo, dist) in enumerate(self._tramos, 1):
            lineas.append(f"\n>> TRAMO #{i}: Medio: {medio_tramo.upper()} | Distancia: {dist} km")
            
            mensaje_cambio = anfibio.cambiar_medio(medio_tramo)
            lineas.append(f"   {mensaje_cambio}")
            lineas.append(f"   Modo de propulsión: {anfibio.operar_propulsion()}")

            v_max = anfibio.calcular_velocidad_maxima()
            tasa = anfibio.calcular_tasa_consumo()
            consumo_tramo = anfibio.desplazarse(dist)
            consumo_acumulado_viaje += consumo_tramo

            lineas.append(f"   Velocidad Máxima en este medio : {v_max:>8.2f} km/h")
            lineas.append(f"   Tasa de Consumo en este medio  : {tasa:>8.4f} L/km")
            lineas.append(f"   Combustible Consumido en tramo : {consumo_tramo:>8.2f} L")

        lineas.append("\n" + "-" * 85)
        lineas.append(f"RESUMEN FINAL DEL VIAJE ({len(self._tramos)} tramos):")
        lineas.append(f"• Consumo Total en la Travesía: {consumo_acumulado_viaje:.2f} Litros")
        lineas.append(f"• Consumo Histórico Total del Vehículo: {anfibio.combustible_consumido_total:.2f} Litros")
        lineas.append("=" * 85)

        return "\n".join(lineas)
