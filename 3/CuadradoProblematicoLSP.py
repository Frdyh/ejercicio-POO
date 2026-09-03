from Rectangulo import Rectangulo


class CuadradoProblematicoLSP(Rectangulo):


    def __init__(self, lado: float, nombre: str = "Cuadrado Problemático"):
        super().__init__(ancho=lado, alto=lado, nombre=nombre)

    @property
    def lado(self) -> float:
        return self._ancho

    @Rectangulo.ancho.setter
    def ancho(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("El lado debe ser positivo.")
        self._ancho = float(valor)
        self._alto = float(valor)  # EFECTO COLATERAL: Modifica también el alto, rompiendo LSP

    @Rectangulo.alto.setter
    def alto(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("El lado debe ser positivo.")
        self._ancho = float(valor)  # EFECTO COLATERAL: Modifica también el ancho, rompiendo LSP
        self._alto = float(valor)
