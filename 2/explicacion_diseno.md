# Ejercicio 2: Motor de Vehículos con Restricciones Físicas Contradictorias
**Profesor:** Daniel Moncada  
**Autor:** Solución Arquitectura POO en Python

---

## 1. Justificación del Diseño y Jerarquía

El problema plantea restricciones físicas contradictorias: el rozamiento por rodadura en tierra responde a leyes físicas distintas de la resistencia hidrodinámica del agua o la aerodinámica del aire.

- **`Vehiculo` (Clase Base Abstracta)**: Encapsula atributos universales (`nombre`, `peso_kg`, `potencia_hp`, `medio_actual`, `combustible_consumido_total`) y define el contrato polimórfico mediante `calcular_velocidad_maxima()` y `calcular_tasa_consumo()`.
- **`VehiculoTerrestre`**: Implementa cinemática basada en coeficiente de fricción por rodadura en asfalto/terreno compacto y número de ruedas.
- **`VehiculoAcuatico`**: Implementa cinemática basada en resistencia hidrodinámica del casco, densidad del fluido ($1000\text{ kg/m}^3$) y calado.
- **`VehiculoAereo`**: Modela vuelo horizontal estándar y sustentación aerodinámica.
- **`ComportamientoVTOL`**: Mixin reutilizable que provee empuje vectorial, despegue y aterrizaje vertical sin acoplamiento a una aeronave específica.
- **`VehiculoAereoVTOL`**: Combina la cinemática de `VehiculoAereo` con `ComportamientoVTOL` sin duplicar la lógica de crucero horizontal.
- **`VehiculoAnfibio`**: Modela un vehículo que conmuta en tiempo de ejecución su medio de desplazamiento (`tierra` vs `agua`).

---

## 2. Resolución de Conflictos en `VehiculoAnfibio`

### Conflicto de Métodos Duplicados:
Tanto `VehiculoTerrestre` como `VehiculoAcuatico` implementan `calcular_velocidad_maxima()`, `calcular_tasa_consumo()` y métodos de propulsión específicos.

### Solución Implementada:
1. **Despacho Dinámico Explícito**: En lugar de depender ciegamente del MRO de Python (el cual por defecto favorecería a la primera clase en la lista de herencia), `VehiculoAnfibio` intercepta las llamadas y despacha hacia `VehiculoTerrestre` o `VehiculoAcuatico` según su estado mutable `self._medio_actual`.
2. **Método `cambiar_medio(nuevo_medio)`**: Permite reconfigurar el tren motriz en tiempo de ejecución, actualizando instantáneamente las tasas de consumo y velocidades operativas.

---

## 3. Simulación de Recorrido de Tres Tramos

Se simuló una travesía completa en 3 tramos:
1. **Tramo 1 (Tierra - 80 km)**: Opera como vehículo terrestre (ruedas y fricción terrestre).
2. **Tramo 2 (Agua - 35 km)**: Transiciona a medio acuático (turbinas y resistencia hidrodinámica).
3. **Tramo 3 (Tierra - 45 km)**: Retorna a medio terrestre.

El consumo total acumulado y las variaciones dinámicas de velocidad máxima quedan registrados con total exactitud física.
