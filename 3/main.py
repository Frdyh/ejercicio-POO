from Cuadrado import Cuadrado
from FiguraCompuesta import FiguraCompuesta

c = Cuadrado(5)
print("Area cuadrado:", c.area())
f = FiguraCompuesta()
f.agregar(c)
print("Area compuesta:", f.area())
