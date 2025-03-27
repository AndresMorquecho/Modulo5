from laptop import Laptop
import random
class Laptop_business(Laptop):
    def __init__(self, marca, procesado, memoria, almacenamiento, duracion_bateria, costo=500, impuesto=10):
        super().__init__(marca, procesado, memoria, costo, impuesto)
        self.almacenamiento = almacenamiento
        self.duracion_bateria = duracion_bateria
    
    def realizar_diagnostico_sistema(self):
        resultado_diagnostico= super().realizar_diagnostico_sistema()
        resultado_conectividad = self.verificar_conectividad_red()
        resultado_diagnostico["Diagnostico conectividad"]= resultado_conectividad
        return resultado_diagnostico

    def verificar_conectividad_red(self):
        resultado = {}
        conectividad = ["latencia", "wifi", "acceso a servidores"]
        
        x = 0
        for i in conectividad:
            if x == 0 :
                valor = random.choice(["90","80","60"])
            elif x == 1:
                valor = random.choice(["Acceso", "Sin acceso"])
            else:
                valor = random.choice(["Acceso", "Sin acceso"])
            
            resultado[i] = valor            
            x +=1 
        return resultado
    def __str__(self):
        return (

        f" {'Marca:':<15} {self.marca:<15} \n"
        f" {'Procesador:':<15} {self.procesado:<15} \n"
        f" {'Memoria:':<15} {self.memoria:<15} \n"
        f" {'Almacenamiento:':<15} {self.almacenamiento:<15} \n"
        f" {'Duración Batería:':<15} {self.duracion_bateria:<15} \n"
        f" {'Costo:':<15} ${self.costo:<14} \n"
        f" {'Impuesto:':<15} {self.impuesto}%{'':<13} \n"
 
    )