# Ejercicio 3: Figuras Geométricas con Herencia, Covarianza y Principio de Liskov (LSP)
**Profesor:** Daniel Moncada  
**Autor:** Solución Arquitectura POO en Python

---

## 1. Demostración y Justificación de Ruptura de Liskov (LSP)

### El Problema de `Cuadrado extends Rectangulo`:
El Principio de Sustitución de Liskov establece que si $S$ es un subtipo de $T$, cualquier programa que use $T$ debe poder usar instancias de $S$ sin alterar la corrección del comportamiento esperado.

- En un `Rectangulo`, las dimensiones `ancho` y `alto` son independientes:
  $$\text{Si } r.ancho \leftarrow 10 \text{ y } r.alto \leftarrow 5 \implies \text{Área} = 50$$
- Si `Cuadrado` hereda de `Rectangulo` y fuerza la invariante $ancho = alto$ modificando ambos atributos al invocar cualquiera de los setters, al ejecutar $r.alto \leftarrow 5$, el ancho se convierte en $5$, produciendo un área de $25$ en lugar de $50$.
- **Conclusión**: `Cuadrado` rompe el contrato y la post-condición de `Rectangulo`.

### Rediseño Correcto:
Se desacopla `Cuadrado` de `Rectangulo`. Ambas clases derivan directamente de la abstracción pura `Figura`, exponiendo únicamente sus propiedades intrínsecas (`lado` para `Cuadrado`, y `ancho`/`alto` para `Rectangulo`).

---

## 2. Covarianza en el Tipo de Retorno

- En la clase base `Figura`, se define el método `escalar(factor)` parametrizado mediante `TypeVar("T", bound="Figura")` y `typing.Self`.
- Cada subtipo concreto (`Rectangulo`, `Cuadrado`, `Circulo`, `FiguraCompuesta`) implementa `escalar(factor)` retornando una nueva instancia de su **mismo tipo concreto**.

---

## 3. Patrón Composite y Recursión en 3 Niveles

La clase `FiguraCompuesta` almacena una colección de objetos de tipo `Figura` (pudiendo anidar a su vez otras figuras compuestas):
- **Cálculo de Área y Perímetro**: Se ejecuta de manera recursiva a través del árbol de composición.
- **Escalado Recursivo**: `escalar(factor)` invoca recursivamente `f.escalar(factor)` en cada hijo, devolviendo una nueva `FiguraCompuesta` estructurada idénticamente pero escalada en todas sus dimensiones.
- **Estructura Evaluada**:
  - **Nivel 1 (Raíz)**: Círculo ($r=5$), Rectángulo ($10\times 4$) y Módulo Nivel 2.
  - **Nivel 2**: Cuadrado ($l=6$), Círculo ($r=3$) y Sub-ensamble Nivel 3.
  - **Nivel 3**: Rectángulo ($3\times 8$), Cuadrado ($l=4$) y Círculo ($r=2$).
  - **Total**: 7 figuras distintas anidadas en 3 niveles de profundidad.
