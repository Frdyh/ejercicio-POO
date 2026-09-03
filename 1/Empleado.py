class Empleado:
    def __init__(self, id_empleado, nombre, salario_base):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.salario_base = salario_base
    def calcular_salario(self):
        return self.salario_base
