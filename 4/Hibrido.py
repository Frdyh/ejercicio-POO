from Personaje import Personaje

class Hibrido(Personaje):
    def __init__(self, hp, mana):
        Personaje.__init__(self, hp)
        self.mana = mana
    def atacar(self):
    
        if self.esta_aturdido:
            print("Hibrido aturdido")
            return 0
        if self.mana > 10:
            self.mana -= 10
            return 20 
        else:
            return 10 
