from Personaje import Personaje

class Mago(Personaje):


    COSTE_MANA_HECHIZO = 25.0

    def __init__(
        self,
        nombre: str,
        salud_maxima: float = 100.0,
        mana_maximo: float = 90.0,
        ataque_base: float = 12.0,
        defensa: float = 6.0,
        poder_magico: float = 38.0,
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
        self._poder_magico = poder_magico

    def atacar_magico(self, objetivo: Personaje) -> str:
        """Lógica de ataque arcano de Mago con consumo de maná."""
        if self.consumir_mana(self.COSTE_MANA_HECHIZO):
  
            danio_magico = self._poder_magico
            danio_infligido = objetivo.recibir_danio(danio_magico, ignorar_defensa=True)
            return (
                f"[MAGO] {self.nombre} conjura 'Llama Arcana' (-{self.COSTE_MANA_HECHIZO:.0f} MP) sobre {objetivo.nombre}, "
                f"infligiendo {danio_infligido:.1f} de daño mágico puro (MP restante: {self.mana_actual:.1f}, HP obj: {objetivo.salud_actual:.1f})"
            )
        else:

            danio_infligido = objetivo.recibir_danio(self.ataque_base)
            return (
                f"[MAGO] {self.nombre} no tiene maná suficiente y golpea con su báculo a {objetivo.nombre}, "
                f"infligiendo {danio_infligido:.1f} de daño físico débil (HP obj: {objetivo.salud_actual:.1f})"
            )

    def atacar(self, objetivo: Personaje) -> str:
        return self.atacar_magico(objetivo)
