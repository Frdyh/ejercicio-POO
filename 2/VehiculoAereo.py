import math
from Vehiculo import Vehiculo


class VehiculoAereo(Vehiculo):
    """
    Vehículo adaptado para desplazarse por el aire en vuelo horizontal estándar.
    """

    DENSIDAD_AIRE_CRUCERO = 1.225  # kg/m^3
    COEF_AERODINAMICO = 0.035

    def __init__(self, nombre: str, peso_kg: float, potencia_hp: float, envergadura_m: float = 12.0, **kwargs):
        super().__init__(
            nombre=nombre,
            peso_kg=peso_kg,
            potencia_hp=potencia_hp,
            medio_actual="aire",
            **kwargs
        )
        self._envergadura_m = max(1.0, envergadura_m)
        self._en_vuelo = False

    @property
    def envergadura_m(self) -> float:
        return self._envergadura_m

    @property
    def en_vuelo(self) -> bool:
        return self._en_vuelo

    def calcular_velocidad_maxima(self) -> float:
        """
        Velocidad máxima aérea (km/h):
        En el aire la resistencia es menor a altas potencias comparado con agua o fricción de rodadura.
        """
        velocidad = math.sqrt((self.potencia_hp * 1200.0) / (self.COEF_AERODINAMICO * self.peso_kg)) * 5.2
        return round(velocidad, 2)

    def calcular_tasa_consumo(self) -> float:
        """
        Consumo en crucero aéreo (L/km).
        """
        tasa = (0.00012 * self.peso_kg) + (0.00045 * self.potencia_hp)
        return round(tasa, 4)

    def despegar_convencional(self, longitud_pista_m: float = 800.0) -> str:
        """
        Despegue convencional mediante carreteo por pista horizontal.
        """
        self._en_vuelo = True
        return f"{self.nombre}: Carreteo en pista de {longitud_pista_m}m y despegue aerodinámico estándar completado."

    def aterrizar_convencional(self) -> str:
        self._en_vuelo = False
        return f"{self.nombre}: Aterrizaje sobre pista con rodaje horizontal completado."
