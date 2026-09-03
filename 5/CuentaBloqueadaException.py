from ExcepcionTransaccion import ExcepcionTransaccion
from NivelSeveridad import NivelSeveridad

class CuentaBloqueadaException(ExcepcionTransaccion):


    def __init__(
        self,
        id_transaccion: str,
        cuenta_origen: str,
        monto: float,
        motivo_bloqueo: str = "Bloqueo preventivo por seguridad",
        **kwargs
    ):
        mensaje = f"Operación denegada. La cuenta {cuenta_origen} se encuentra bloqueada. Motivo: {motivo_bloqueo}"
        super().__init__(
            mensaje=mensaje,
            id_transaccion=id_transaccion,
            cuenta_origen=cuenta_origen,
            monto=monto,
            codigo_error="ERR-TX-103",
            severidad=NivelSeveridad.ALTA,
            requiere_notificacion_fraude=False,
            detalles_adicionales={"motivo_bloqueo": motivo_bloqueo},
            **kwargs
        )
        self.motivo_bloqueo = motivo_bloqueo
