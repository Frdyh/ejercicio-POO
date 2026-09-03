from Personaje import Personaje


class Guerrero(Personaje):


    def __init__(
        self,
        nombre: str,
        salud_maxima: float = 160.0,
        mana_maximo: float = 20.0,
        ataque_base: float = 28.0,
        defensa: float = 12.0,
        furia_critica: float = 1.35,
        **kwargs
    ):
        super().__init__(
            nombre=nombre,
            salud_maxima=salud_maxima,
            mana_maximo=mana_maximo,
            ataque_base=ataque_base,
            defensa=defensa,
            **kwargs
        )
        self._furia_critica = furia_critica

    def atacar_fisico(self, objetivo: Personaje) -> str:
  
        danio = self.ataque_base * self._furia_critica
        danio_infligido = objetivo.recibir_danio(danio)
        return (
            f"[GUERRERO] {self.nombre} blande su mandoble y ejecuta 'Tajo Brutal' sobre {objetivo.nombre}, "
            f"infligiendo {danio_infligido:.1f} de daño físico (HP restante: {objetivo.salud_actual:.1f})"
        )

    def atacar(self, objetivo: Personaje) -> str:
        return self.atacar_fisico(objetivo)
