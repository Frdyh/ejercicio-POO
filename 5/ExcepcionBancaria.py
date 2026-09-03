import datetime
from typing import Optional, Dict, Any
from NivelSeveridad import NivelSeveridad

class ExcepcionBancaria(Exception):
    def __init__(
        self,
        mensaje: str,
        codigo_error: str = "ERR-BNK-000",
        severidad: NivelSeveridad = NivelSeveridad.BAJA,
        requiere_notificacion_fraude: bool = False,
        detalles_adicionales: Optional[Dict[str, Any]] = None,
        **kwargs
    ):
        super().__init__(mensaje)
        self.mensaje = mensaje
        self.codigo_error = codigo_error
        self.severidad = severidad
        self.requiere_notificacion_fraude = requiere_notificacion_fraude
        self.timestamp = datetime.datetime.now()
        self.detalles_adicionales = detalles_adicionales or {}

    def obtener_metadatos(self) -> Dict[str, Any]:
        return {
            "Tipo": self.__class__.__name__,
            "Mensaje": self.mensaje,
            "Codigo Error": self.codigo_error,
            "Severidad": str(self.severidad),
            "Notificar a Fraude": "SI" if self.requiere_notificacion_fraude else "NO",
            "Timestamp": self.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "Detalles": self.detalles_adicionales
        }

    def __str__(self) -> str:
        return f"[{self.codigo_error}] [{self.severidad}] {self.mensaje}"
