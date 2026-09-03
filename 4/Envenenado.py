from Estado import Estado
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Personaje import Personaje

class Envenenado(Estado):

    def __init__(self, duracion_turnos: int = 3, danio_por_turno: float = 12.0):
        super().__init__(nombre="Envenenado", duracion_turnos=duracion_turnos, prioridad=1)
        self._danio_por_turno = danio_por_turno

    @property
    def danio_por_turno(self) -> float:
        return self._danio_por_turno

    def al_iniciar_turno(self, personaje: "Personaje") -> str:
        personaje.recibir_danio(self._danio_por_turno, ignorar_defensa=True)
        return f"[VENENO] El veneno corroe a {personaje.nombre}, causando {self._danio_por_turno:.1f} de daño directo!"

    def puede_actuar(self) -> bool:
        return True
