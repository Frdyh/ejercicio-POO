from Figura import Figura
class FiguraCompuesta(Figura):

    def __init__(self):
        self.lista = [] 

    def agregar(self, figura):
        self.lista.append(figura)

    def area(self):
        total = 0
        for f in self.lista:
            total += f.area()
        return total
