from Medico import Medico
from Residente import Residente

class MedicoResidenteInvestigador(Medico, Residente):
    # El estudiante no sabe usar super() bien, asi que llama a ambos inits
    def __init__(self, id_empleado, nombre, salario_base, especialidad, anio_residencia):
        Medico.__init__(self, id_empleado, nombre, salario_base, especialidad)
        Residente.__init__(self, id_empleado, nombre, salario_base, anio_residencia)
    
    def calcular_salario(self):
        # Suma los dos o hace un calculo raro hardcodeado
        return Medico.calcular_salario(self) + 500
