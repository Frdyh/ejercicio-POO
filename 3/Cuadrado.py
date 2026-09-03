from Rectangulo import Rectangulo
class Cuadrado(Rectangulo):

    def __init__(self, lado):
        Rectangulo.__init__(self, lado, lado)
    def set_lado(self, lado):
        self.base = lado
        self.altura = lado
