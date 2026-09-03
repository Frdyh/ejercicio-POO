from enum import Enum

class NivelSeveridad(Enum):
    BAJA = "BAJA"
    MEDIA = "MEDIA"
    ALTA = "ALTA"
    CRITICA = "CRITICA"

    def __str__(self) -> str:
        return self.value
