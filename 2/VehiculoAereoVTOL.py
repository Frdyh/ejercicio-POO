from VehiculoAereo import VehiculoAereo
from ComportamientoVTOL import ComportamientoVTOL


class VehiculoAereoVTOL(VehiculoAereo, ComportamientoVTOL):
    """
    Aeronave que combina la aerodinámica y vuelo horizontal de VehiculoAereo
    con las capacidades de despegue/aterrizaje vertical de ComportamientoVTOL,
    evitando cualquier duplicación de código.
    """

    def __init__(
        self,
        nombre: str,
        peso_kg: float,
        potencia_hp: float,
        envergadura_m: float = 10.5,
        empuje_vectorial_kn: float = 90.0,
        **kwargs
    ):
        super().__init__(
            nombre=nombre,
            peso_kg=peso_kg,
            potencia_hp=potencia_hp,
            envergadura_m=envergadura_m,
            empuje_vectorial_kn=empuje_vectorial_kn,
            **kwargs
        )

    def iniciar_mision_vtol(self) -> str:
        reporte_despegue = self.despegue_vertical()
        self._en_vuelo = True
        return f"[{self.nombre}] {reporte_despegue} | Velocidad de crucero horizontal estimada: {self.calcular_velocidad_maxima()} km/h"
