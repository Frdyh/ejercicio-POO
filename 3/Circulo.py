import math
from typing import Self
from Figura import Figura


class Circulo(Figura):


    def __init__(self, radio: float, nombre: str = "Círculo"):
        super().__init__(nombre=nombre)
        if radio <= 0:
            raise ValueError("El radio del círculo debe ser positivo.")
        self._radio = float(radio)

    @property
    def radio(self) -> float:
        return self._radio

    @radio.setter
    def radio(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("El radio debe ser positivo.")
        self._radio = float(valor)

    def area(self) -> float:
        return round(math.pi * (self._radio ** 2), 4)

    def perimetro(self) -> float:
        return round(2.0 * math.pi * self._radio, 4)

    def escalar(self, factor: float) -> Self:
        if factor <= 0:
            raise ValueError("El factor de escala debe ser mayor a 0.")
        return Circulo(self._radio * factor, nombre=f"{self.nombre} (x{factor})")

    def __repr__(self) -> str:
        return f"Circulo(radio={self.radio})"
