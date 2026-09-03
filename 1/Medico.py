from Empleado import Empleado
class Medico(Empleado):
    def __init__(self, id_empleado, nombre, salario_base, especialidad):
        # ERROR COMUN: llamar explicitamente a Empleado.__init__
        Empleado.__init__(self, id_empleado, nombre, salario_base)
        self.especialidad = especialidad
        self.horas_extra = 0
    def calcular_salario(self):
        return self.salario_base + (self.horas_extra * 50)
