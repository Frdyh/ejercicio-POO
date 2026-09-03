# Ejercicio 4: Jerarquía de Personajes de Videojuego con Estados Mutables
**Profesor:** Daniel Moncada  
**Autor:** Solución Arquitectura POO en Python

---

## 1. Justificación del Diseño y Manejo de Estados Mutables

En los videojuegos, aplicar efectos temporales (buffs/debuffs como Veneno o Aturdimiento) modificando la clase original del personaje es un antipatrón que rompe el principio de responsabilidad única y la herencia rígida.

### Solución Arquitectónica (Patrón State / Strategy / Decorator):
- **`Personaje` (Clase Base Abstracta)**: Administra atributos vitales (`salud`, `mana`, `defensa`, `ataque_base`) y mantiene una colección dinámica `_estados_activos: List[Estado]`.
- **`Estado` (Clase Base de Efectos)**: Define el contrato temporal con `duracion_turnos`, `prioridad`, y hooks:
  - `al_iniciar_turno(personaje)`: Aplica efectos pasivos (daño continuo, regeneración, etc.).
  - `puede_actuar()`: Retorna un booleano indicando si el estado incapacita la acción ofensiva.
- **`Envenenado`**: Estado con prioridad 1 que inflige daño directo periódico ignorando la defensa pasiva.
- **`Aturdido`**: Estado de control de masas con prioridad 2 que bloquea `puede_actuar() -> False`.

---

## 2. Resolución de Conflicto de Métodos en `Hibrido`

- **Jerarquía Múltiple**: `Hibrido` hereda tanto de `Guerrero` como de `Mago`.
- **Conflicto en `atacar()`**: Ambas superclases poseen comportamientos de ataque divergentes (físico sin coste de maná vs mágico de alto impacto con coste de maná).
- **Despacho Dinámico en Tiempo de Ejecución**: `Hibrido` sobrescribe `atacar(objetivo)` y evalúa:
  ```python
  if self._mana_actual >= Mago.COSTE_MANA_HECHIZO:
      return Mago.atacar_magico(self, objetivo)
  else:
      return Guerrero.atacar_fisico(self, objetivo)
  ```
  Esto permite optimizar el daño cuando hay recursos y conmutar a la fuerza física cuando el maná se agota, sin romper el polimorfismo.

---

## 3. Justificación del Caso Límite: Envenenado mientras está Aturdido

Cuando un personaje sufre simultáneamente envenenamiento y aturdimiento, el orden de resolución es crítico y se estructura en tres fases cronológicas:
1. **Fase 1 (Efectos Pasivos - Prioridad 1)**: El veneno se aplica al comienzo del turno. Si el personaje muere por el daño del veneno, el combate finaliza inmediatamente, ahorrando cómputo de acciones.
2. **Fase 2 (Control de Masas - Prioridad 2)**: Si el personaje sobrevive, se verifica `puede_actuar()`. La presencia de `Aturdido` inhabilita al personaje de ejecutar su ataque en ese turno.
3. **Fase 3 (Disipación y Tick)**: Se reduce en 1 la duración de ambos estados y se eliminan aquellos que llegan a 0.
