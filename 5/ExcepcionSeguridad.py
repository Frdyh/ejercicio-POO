from typing import Optional, Dict, Any
from ExcepcionBancaria import ExcepcionBancaria
from NivelSeveridad import NivelSeveridad

class ExcepcionSeguridad(ExcepcionBancaria):
    def __init__(
        self,
        mensaje: str,
        ip_origen: str,
        nivel_riesgo: str = "ALTO",
        codigo_error: str = "ERR-SEC-200",
        severidad: NivelSeveridad = NivelSeveridad.CRITICA,
        requiere_notificacion_fraude: bool = True,
        detalles_adicionales: Optional[Dict[str, Any]] = None,
        **kwargs
    ):
        super().__init__(
            mensaje=mensaje,
            codigo_error=codigo_error,
            severidad=severidad,
            requiere_notificacion_fraude=requiere_notificacion_fraude,
            detalles_adicionales=detalles_adicionales,
            **kwargs
        )
        self.ip_origen = ip_origen
        self.nivel_riesgo = nivel_riesgo

    def obtener_metadatos(self) -> Dict[str, Any]:
        meta = super().obtener_metadatos()
        meta.update({
            "IP Origen": self.ip_origen,
            "Nivel de Riesgo": self.nivel_riesgo
        })
        return meta
