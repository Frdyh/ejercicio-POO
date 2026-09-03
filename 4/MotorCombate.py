from typing import List
from Personaje import Personaje

class MotorCombate:

    def __init__(self, luchador_a: Personaje, luchador_b: Personaje):
        self.luchador_a = luchador_a
        self.luchador_b = luchador_b
        self.registro_eventos: List[str] = []

    def simular_duelo(self, max_turnos: int = 15) -> str:
        lineas = [
            "=" * 85,
            f"INICIO DEL COMBATE POR TURNOS: {self.luchador_a.nombre} VS {self.luchador_b.nombre}",
            "=" * 85,
            f"* Luchador 1: {self.luchador_a}",
            f"* Luchador 2: {self.luchador_b}",
            "-" * 85,
        ]

        turno_actual = 1
        atacante = self.luchador_a
        defensor = self.luchador_b

        while self.luchador_a.esta_vivo() and self.luchador_b.esta_vivo() and turno_actual <= max_turnos:
            lineas.append(f"\n--- TURNO #{turno_actual} | Turno de: {atacante.nombre} ({atacante.__class__.__name__}) ---")


            mensajes_inicio = atacante.procesar_fase_inicio_turno()
            for msg in mensajes_inicio:
                lineas.append(f"  [FASE INICIO ESTADOS] {msg}")

       
            if not atacante.esta_vivo():
                lineas.append(f"  [FIN] {atacante.nombre} no sobrevive a la fase de estados.")
                break

          
            if atacante.puede_actuar():
                resultado_ataque = atacante.atacar(defensor)
                lineas.append(f"  [ACCION] {resultado_ataque}")
            else:
                lineas.append(f"  [INCAPACITADO] {atacante.nombre} esta aturdido/impedido y PIERDE su accion este turno.")

         
            mensajes_fin = atacante.procesar_fase_fin_turno()
            for msg in mensajes_fin:
                lineas.append(f"  [FASE FIN ESTADOS] {msg}")


            if not defensor.esta_vivo():
                lineas.append(f"  [VICTORIA] {defensor.nombre} ha caido en combate. {atacante.nombre} es el vencedor!")
                break

            lineas.append(f"  [ESTADO] {atacante.nombre} (HP: {atacante.salud_actual:.1f}) | {defensor.nombre} (HP: {defensor.salud_actual:.1f})")

            atacante, defensor = defensor, atacante
            turno_actual += 1

        lineas.append("\n" + "=" * 85)
        lineas.append("FIN DEL ENCUENTRO")
        lineas.append(f"Resultado Final:")
        lineas.append(f"  * {self.luchador_a}")
        lineas.append(f"  * {self.luchador_b}")
        lineas.append("=" * 85)

        return "\n".join(lineas)
