from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Personaje import Personaje


class Estado(ABC):

    def __init__(self, nombre: str, duracion_turnos: int, prioridad: int = 10):
        self._nombre = nombre
        self._duracion_turnos = max(1, duracion_turnos)
        self._prioridad = prioridad  # Menor número = mayor prioridad de resolución

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def duracion_turnos(self) -> int:
        return self._duracion_turnos

    @property
    def prioridad(self) -> int:
        return self._prioridad

    @abstractmethod
    def al_iniciar_turno(self, personaje: "Personaje") -> str:
        """Efecto pasivo que se ejecuta al inicio del turno del personaje."""
        pass

    def puede_actuar(self) -> bool:
        """Determina si este estado permite al personaje ejecutar acciones ofensivas."""
        return True

    def modificar_danio_emitido(self, danio: float) -> float:
        """Permite a los estados modular el daño emitido."""
        return danio

    def tick_duracion(self) -> bool:
        """
        Reduce en 1 la duración del estado.
        Retorna True si el estado ha expirado (duracion <= 0).
        """
        self._duracion_turnos -= 1
        return self._duracion_turnos <= 0

    def __str__(self) -> str:
        return f"{self.nombre} ({self.duracion_turnos} turnos restantes)"
