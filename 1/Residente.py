from Empleado import Empleado
class Residente(Empleado):
    def __init__(self, id_empleado, nombre, salario_base, anio_residencia):
        Empleado.__init__(self, id_empleado, nombre, salario_base)
        self.anio_residencia = anio_residencia
    def calcular_salario(self):
        return self.salario_base + (self.salario_base * 0.05 * self.anio_residencia)
