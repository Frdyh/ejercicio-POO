from ExcepcionTransaccion import ExcepcionTransaccion
from NivelSeveridad import NivelSeveridad


class SaldoInsuficienteException(ExcepcionTransaccion):

    def __init__(
        self,
        id_transaccion: str,
        cuenta_origen: str,
        monto: float,
        saldo_disponible: float,
        **kwargs
    ):
        mensaje = (
            f"Fondos insuficientes en la cuenta {cuenta_origen}. "
            f"Saldo disponible: ${saldo_disponible:,.2f} | Monto requerido: ${monto:,.2f}"
        )
        super().__init__(
            mensaje=mensaje,
            id_transaccion=id_transaccion,
            cuenta_origen=cuenta_origen,
            monto=monto,
            codigo_error="ERR-TX-101",
            severidad=NivelSeveridad.BAJA,
            requiere_notificacion_fraude=False,
            detalles_adicionales={
                "saldo_disponible": saldo_disponible,
                "defasaje": round(monto - saldo_disponible, 2)
            },
            **kwargs
        )
        self.saldo_disponible = float(saldo_disponible)
