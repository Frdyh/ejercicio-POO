from typing import Optional, Dict, Any
from ExcepcionBancaria import ExcepcionBancaria
from NivelSeveridad import NivelSeveridad

class ExcepcionTransaccion(ExcepcionBancaria):
    def __init__(
        self,
        mensaje: str,
        id_transaccion: str,
        cuenta_origen: str,
        monto: float,
        codigo_error: str = "ERR-TX-100",
        severidad: NivelSeveridad = NivelSeveridad.MEDIA,
        requiere_notificacion_fraude: bool = False,
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
        self.id_transaccion = id_transaccion
        self.cuenta_origen = cuenta_origen
        self.monto = float(monto)

    def obtener_metadatos(self) -> Dict[str, Any]:
        meta = super().obtener_metadatos()
        meta.update({
            "ID Transaccion": self.id_transaccion,
            "Cuenta Origen": self.cuenta_origen,
            "Monto": f"${self.monto:,.2f}"
        })
        return meta
