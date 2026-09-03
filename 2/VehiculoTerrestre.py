from Vehiculo import Vehiculo
class VehiculoTerrestre(Vehiculo):
    def __init__(self, marca, llantas):
        Vehiculo.__init__(self, marca)
        self.llantas = llantas
