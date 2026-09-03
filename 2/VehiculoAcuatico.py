from Vehiculo import Vehiculo
class VehiculoAcuatico(Vehiculo):
    def __init__(self, marca, helices):
        Vehiculo.__init__(self, marca)
        self.helices = helices
