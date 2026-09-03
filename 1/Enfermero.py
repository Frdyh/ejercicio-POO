from Empleado import Empleado


class Enfermero(Empleado):
    """
    Clase que representa a un personal de enfermería.
    Regla de negocio: Los turnos rotativos afectan el cálculo de horas nocturnas,
    pero ÚNICAMENTE si trabajan en la Unidad de Cuidados Intensivos (UCI).
    """

    def __init__(
        self,
        id_empleado: str,
        nombre: str,
        salario_base: float,
        trabaja_en_uci: bool = False,
        turnos_rotativos: bool = False,
        horas_nocturnas: float = 0.0,
        tarifa_hora_nocturna: float = 35.0,
        recargo_rotativo_uci: float = 0.30,  # 30% extra si rotativo en UCI
        **kwargs
    ):
        super().__init__(
            id_empleado=id_empleado,
            nombre=nombre,
            salario_base=salario_base,
            **kwargs
        )
        self._trabaja_en_uci = trabaja_en_uci
        self._turnos_rotativos = turnos_rotativos
        self._horas_nocturnas = max(0.0, horas_nocturnas)
        self._tarifa_hora_nocturna = tarifa_hora_nocturna
        self._recargo_rotativo_uci = recargo_rotativo_uci

    @property
    def trabaja_en_uci(self) -> bool:
        return self._trabaja_en_uci

    @trabaja_en_uci.setter
    def trabaja_en_uci(self, valor: bool) -> None:
        self._trabaja_en_uci = bool(valor)

    @property
    def turnos_rotativos(self) -> bool:
        return self._turnos_rotativos

    @turnos_rotativos.setter
    def turnos_rotativos(self, valor: bool) -> None:
        self._turnos_rotativos = bool(valor)

    @property
    def horas_nocturnas(self) -> float:
        return self._horas_nocturnas

    @horas_nocturnas.setter
    def horas_nocturnas(self, valor: float) -> None:
        if valor < 0:
            raise ValueError("Las horas nocturnas no pueden ser negativas.")
        self._horas_nocturnas = valor

    def calcular_tarifa_efectiva_nocturna(self) -> float:
        """
        Calcula la tarifa horaria nocturna considerando si aplica el recargo de UCI con rotación.
        """
        tarifa = self._tarifa_hora_nocturna
        if self.trabaja_en_uci and self.turnos_rotativos:
            tarifa *= (1.0 + self._recargo_rotativo_uci)
        return tarifa

    def calcular_pago_horas_nocturnas(self) -> float:
        return self.horas_nocturnas * self.calcular_tarifa_efectiva_nocturna()

    def calcular_salario_total(self) -> float:
        return self.salario_base + self.calcular_pago_horas_nocturnas()

    def obtener_desglose_nomina(self) -> dict:
        aplica_recargo = self.trabaja_en_uci and self.turnos_rotativos
        return {
            "ID": self.id_empleado,
            "Nombre": self.nombre,
            "Cargo": "Enfermero(a)",
            "UCI": "Sí" if self.trabaja_en_uci else "No",
            "Turnos Rotativos": "Sí" if self.turnos_rotativos else "No",
            "Aplica Recargo Nocturno UCI": "Sí (+30%)" if aplica_recargo else "No (Estándar)",
            "Salario Base": round(self.salario_base, 2),
            "Horas Nocturnas": self.horas_nocturnas,
            "Pago Horas Nocturnas": round(self.calcular_pago_horas_nocturnas(), 2),
            "Salario Total": round(self.calcular_salario_total(), 2),
        }
