from TransaccionSospechosaException import TransaccionSospechosaException
class ServicioBancario:
    def procesar(self, monto, saldo):
        if monto > saldo:
            raise Exception("Saldo insuficiente") 
        if monto > 10000:
            raise TransaccionSospechosaException("Es muy grande")
        print("Exito")
