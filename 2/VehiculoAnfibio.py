from VehiculoTerrestre import VehiculoTerrestre
from VehiculoAcuatico import VehiculoAcuatico

class VehiculoAnfibio(VehiculoTerrestre, VehiculoAcuatico):
    def __init__(self, marca, llantas, helices):
        VehiculoTerrestre.__init__(self, marca, llantas)
        VehiculoAcuatico.__init__(self, marca, helices)
        self.modo = "tierra" # hardcoded string envés de state pattern
    
    def cambiar_modo(self):
        if self.modo == "tierra":
            self.modo = "agua"
        else:
            self.modo = "tierra"
