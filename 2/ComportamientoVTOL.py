from abc import ABC


class ComportamientoVTOL(ABC):
    """
    Mixin / Interfaz de comportamiento que dota a una aeronave de capacidad de despegue y
    aterrizaje vertical (Vertical Take-Off and Landing).
    Permite reutilizar lógica de empuje vectorial o rotores basculantes sin duplicar
    la cinemática de vuelo horizontal.
    """

    def __init__(self, empuje_vectorial_kn: float = 85.0, **kwargs):
        super().__init__(**kwargs)
        self._empuje_vectorial_kn = empuje_vectorial_kn
        self._modo_hover_activo = False

    @property
    def empuje_vectorial_kn(self) -> float:
        return self._empuje_vectorial_kn

    @property
    def modo_hover_activo(self) -> bool:
        return self._modo_hover_activo

    def despegue_vertical(self) -> str:
        """
        Ejecuta despegue vertical sin necesidad de pista de rodaje.
        """
        self._modo_hover_activo = True
        return (
            f"VTOL: Activando toberas basculantes ({self._empuje_vectorial_kn} kN). "
            f"Elevación vertical a 50m y transición a vuelo horizontal completada."
        )

    def aterrizaje_vertical(self) -> str:
        """
        Ejecuta descenso y posado vertical en helipuerto o superficie confinada.
        """
        self._modo_hover_activo = False
        return "VTOL: Deceleración en estacionario y descenso vertical completado con éxito."
