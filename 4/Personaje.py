class Personaje:
    def __init__(self, hp):
        self.hp = hp
        self.esta_envenenado = False
        self.esta_aturdido = False
        self.turnos_veneno = 0
        
    def atacar(self):
        if self.esta_aturdido:
            print("No puedo atacar estoy aturdido")
            return 0
        return 10
