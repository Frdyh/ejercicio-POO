from Empleado import Empleado


class Administrativo(Empleado):


    def __init__(
        self,
        id_empleado: str,
        nombre: str,
        salario_base: float,
        departamento: str,
        bono_gestion: float = 0.0,
        **kwargs
    ):
        super().__init__(
            id_empleado=id_empleado,
            nombre=nombre,
            salario_base=salario_base,
            **kwargs
        )
        self._departamento = departamento
        self._bono_gestion = max(0.0, bono_gestion)

    @property
    def departamento(self) -> str:
        return self._departamento

    @departamento.setter
    def departamento(self, depto: str) -> None:
        if not depto:
            raise ValueError("El departamento no puede estar vacío.")
        self._departamento = depto

    @property
    def bono_gestion(self) -> float:
        return self._bono_gestion

    @bono_gestion.setter
    def bono_gestion(self, bono: float) -> None:
        if bono < 0:
            raise ValueError("El bono de gestión no puede ser negativo.")
        self._bono_gestion = bono

    def calcular_salario_total(self) -> float:
        return self.salario_base + self.bono_gestion

    def obtener_desglose_nomina(self) -> dict:
        return {
            "ID": self.id_empleado,
            "Nombre": self.nombre,
            "Cargo": "Personal Administrativo",
            "Departamento": self.departamento,
            "Salario Base": round(self.salario_base, 2),
            "Bono Gestión": round(self.bono_gestion, 2),
            "Salario Total": round(self.calcular_salario_total(), 2),
        }
