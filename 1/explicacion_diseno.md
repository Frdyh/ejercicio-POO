# Ejercicio 1: Sistema de Nómina Hospitalaria con Reglas Cruzadas
**Profesor:** Daniel Moncada  
**Autor:** Solución Arquitectura POO en Python

---

## 1. Justificación del Diseño y Jerarquía de Clases

El sistema modela una nómina hospitalaria compleja donde conviven diferentes perfiles profesionales con normativas contractuales heterogéneas:

- **`Empleado` (Clase Base Abstracta)**: Declara los atributos comunes (`id_empleado`, `nombre`, `salario_base`) y los métodos abstractos `calcular_salario_total()` y `obtener_desglose_nomina()`.
- **`Medico`**: Especialista que gestiona horas extras estándar a tarifa pactada.
- **`Residente`**: Médico en formación cuyo salario base es escalado mediante una tabla porcentual variable según su año lectivo (1º año: 100%, 2º año: 110%, 3º año: 125%, 4º año: 140%), adicionando bonos por guardias médicas.
- **`Enfermero`**: Modela turnos rotativos y horas nocturnas. Implementa la regla condicional cruzada: el recargo nocturno especial (+30%) se otorga **únicamente** si el enfermero trabaja en la Unidad de Cuidados Intensivos (UCI) y tiene turnos rotativos.
- **`Administrativo`**: Empleado con bono por metas de gestión y departamento asignado.
- **`MedicoResidenteInvestigador`**: Hereda de forma simultánea de `Medico` y `Residente`, integrando además actividades de investigación.

---

## 2. Resolución del Problema del Diamante y MRO

### Estructura del Diamante:
```
           [ Empleado ]
           /          \
      [ Medico ]   [ Residente ]
           \          /
    [ MedicoResidenteInvestigador ]
```

### Mecanismo de Resolución:
1. **Algoritmo C3 Linearization (MRO)**: En Python, el orden de búsqueda es:
   `MedicoResidenteInvestigador -> Medico -> Residente -> Empleado -> object`.
2. **Inicialización Cooperativa**: Las llamadas `super().__init__(**kwargs)` con paso de argumentos nombrados garantizan que el constructor base `Empleado.__init__` se ejecute exactamente **una sola vez**, evitando reinicializaciones redundantes o estado inconsistente.
3. **Composición de Salarios**: En `calcular_salario_total()`, se calcula explícitamente el salario base ajustado por año (proveniente de `Residente`), las guardias (de `Residente`), las horas extra (de `Medico` con recargo del 50% si el área de residencia es distinta a la especialidad principal) y la compensación por horas/bonos de investigación científica.

---

## 3. Manejo de Casos Límite Implementados

1. **Cambio de especialidad/año a mitad de ciclo**: Método `cambiar_especialidad_a_mitad_de_ano()` en `Residente`, actualizando área y año, y preservando trazabilidad mediante historial de auditoría.
2. **Regla de área distinta en Médico Residente Investigador**: Si un médico especialista en *Medicina Interna* realiza una residencia en *Oncología*, sus horas extra se pagan automáticamente a una tasa diferenciada (+50%) por mayor complejidad y doble rol.
3. **Validaciones de dominio**: Protección ante años de residencia fuera del intervalo [1, 4], valores negativos en salarios o guardias, y prevención de duplicados de ID en `NominaHospital`.
