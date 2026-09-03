from Figura import Figura
class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return self.base * self.altura
    def escalar(self, factor):
        self.base = self.base * factor
        self.altura = self.altura * factor
        return self
