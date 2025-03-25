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