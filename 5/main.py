from ServicioBancario import ServicioBancario
s = ServicioBancario()
try:
    s.procesar(20000, 1000)
except Exception as e:
    print("Ocurrio un error:", e)
