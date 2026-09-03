# Ejercicio 5: Jerarquía de Excepciones Personalizadas para un Sistema Bancario
**Profesor:** Daniel Moncada  
**Autor:** Solución Arquitectura POO en Python

---

## 1. Diseño de la Jerarquía de Excepciones

El sistema bancario requiere una arquitectura de excepciones desacoplada, tipada y enriquecida con metadatos de auditoría:

```
                  [ Exception ]
                        |
              [ ExcepcionBancaria ]
                 /              \
    [ ExcepcionTransaccion ]   [ ExcepcionSeguridad ]
      /        |        \                \
 [Saldo]   [Limite]  [Bloqueada]          \
      \____________________________________\
                        |
         [ TransaccionSospechosaException ]  <-- Herencia Múltiple
```

- **`ExcepcionBancaria` (Base)**: Provee atributos comunes a todas las excepciones del dominio: `mensaje`, `codigo_error`, `severidad` (`BAJA`, `MEDIA`, `ALTA`, `CRITICA`), `timestamp`, `requiere_notificacion_fraude` y diccionario extensible de `detalles_adicionales`.
- **`ExcepcionTransaccion`**: Incorpora `id_transaccion`, `cuenta_origen` y `monto`.
  - `SaldoInsuficienteException` (Severidad Baja): Error operacional de fondos.
  - `LimiteDiarioExcedidoException` (Severidad Media): Superación de cupo diario.
  - `CuentaBloqueadaException` (Severidad Alta): Operación sobre cuenta restringida.
- **`ExcepcionSeguridad`**: Incorpora `ip_origen`, `nivel_riesgo` y `requiere_notificacion_fraude=True`.
- **`TransaccionSospechosaException`**: Combina mediante **herencia múltiple** las ramas `ExcepcionTransaccion` y `ExcepcionSeguridad`, permitiendo activar protocolos de defensa en el SOC mientras se preservan los datos transaccionales.

---

## 2. Captura y Enriquecimiento Multinivel (Multi-level Enrichment)

Las capas superiores (controladores de API o middleware de auditoría) interceptan las excepciones de las capas de persistencia y dominio, inyectando metadatos contextuales (como `canal_acceso`, `sesion_id` o activación de alertas SOC) sin mutar la esencia de la excepción original.

---

## 3. Justificación del Escenario de Tres Fallos Simultáneos y Cause Chaining

### Escenario:
Una transacción incumple simultáneamente:
1. Saldo disponible insuficiente.
2. Superación del límite diario.
3. Patrón sospechoso (origen desde IP en lista negra y país bloqueado).

### Decisión de Diseño y Justificación:
- **Excepción Concreta Principal Lanzada**: `TransaccionSospechosaException`.
- **Justificación**:
  1. **Principio de Máxima Severidad y Ciberseguridad**: En sistemas financieros, la seguridad y prevención de fraude prevalecen sobre restricciones operacionales de saldo.
  2. **Ofuscación de Información a Atacantes**: Si el sistema informara "Saldo Insuficiente", un actor malicioso sabría que la cuenta existe pero no tiene fondos, sin alertar al equipo de seguridad. Al lanzar `TransaccionSospechosaException`, se gatilla el protocolo de contención del SOC.
  3. **Encadenamiento de Causas (`Cause Chaining` con `raise ... from ...`)**: Mediante el atributo `__cause__` de Python, `TransaccionSospechosaException` encapsula a `LimiteDiarioExcedidoException`, la cual a su vez encapsula a `SaldoInsuficienteException`. Esto permite a los auditores y peritos forenses reconstruir la totalidad del evento sin pérdida de contexto.
