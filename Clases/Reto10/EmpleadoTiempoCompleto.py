from Empleado import Empleado

class EmpleadoTimepoCompleto(Empleado):
    def __init__(self, nombre, salario_base, bono):
        super().__init__(nombre, salario_base)
        self.bono = bono
    
    def calcular_salario(self):
        salario_final = self.salario_base + (self.salario_base * self.bono /100)
        return salario_final
    