from Estado import Estado
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Personaje import Personaje


class Aturdido(Estado):


    def __init__(self, duracion_turnos: int = 2):
        super().__init__(nombre="Aturdido", duracion_turnos=duracion_turnos, prioridad=2)

    def al_iniciar_turno(self, personaje: "Personaje") -> str:
        return f"[ATURDIMIENTO] {personaje.nombre} está aturdido, desorientado e incapaz de reaccionar este turno."

    def puede_actuar(self) -> bool:
        return False
