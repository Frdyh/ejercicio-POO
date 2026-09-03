from ExcepcionTransaccion import ExcepcionTransaccion
from NivelSeveridad import NivelSeveridad

class LimiteDiarioExcedidoException(ExcepcionTransaccion):
    def __init__(
        self,
        id_transaccion: str,
        cuenta_origen: str,
        monto: float,
        limite_diario: float,
        monto_acumulado_hoy: float,
        **kwargs
    ):
        exceso = (monto_acumulado_hoy + monto) - limite_diario
        mensaje = (
            f"Límite diario de transferencias superado en la cuenta {cuenta_origen}. "
            f"Límite: ${limite_diario:,.2f} | Acumulado: ${monto_acumulado_hoy:,.2f} | "
            f"Monto intentado: ${monto:,.2f} | Exceso: ${exceso:,.2f}"
        )
        super().__init__(
            mensaje=mensaje,
            id_transaccion=id_transaccion,
            cuenta_origen=cuenta_origen,
            monto=monto,
            codigo_error="ERR-TX-102",
            severidad=NivelSeveridad.MEDIA,
            requiere_notificacion_fraude=False,
            detalles_adicionales={
                "limite_diario": limite_diario,
                "acumulado_hoy": monto_acumulado_hoy,
                "exceso": round(exceso, 2)
            },
            **kwargs
        )
        self.limite_diario = float(limite_diario)
        self.monto_acumulado_hoy = float(monto_acumulado_hoy)
