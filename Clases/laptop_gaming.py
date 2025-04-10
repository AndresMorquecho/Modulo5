
from laptop import Laptop

class laptop_gaming(Laptop):
    def __init__(self, marca, procesado, memoria,tarj_graf, costo=500, impuesto=10 ):
    
        super().__init__(marca, procesado, memoria, costo, impuesto)
        self.tarj_graf = tarj_graf
        
    def realizar_diagnostico_sistema(self):
        resultado_diagnostico = super().realizar_diagnostico_sistema()
        resultado_juegos = self.resultado_diagnostico_juegos()
        resultado_diagnostico["resultado juegos"] = resultado_juegos
        return resultado_diagnostico
    
    def __str__(self):
        return f" Marca: {self.marca}  \n Procesador: {self.procesado} \n Memoria: {self.memoria} \n  Tarjeta Grafica: {self.tarj_graf} \n costo: {self.costo}\n impuesto {self.impuesto} "
        
        
    def resultado_diagnostico_juegos(self):
        juegos = ["GTA", "MARIOS BROS", "COD"]
        resultados = {}
        for juego in juegos:
            fps_base = 30
            if "RTX" in self.tarj_graf:
                fps = fps_base * 3
            elif "GTX" in self.tarj_graf:
                fps = fps_base * 2
            else:
                fps = fps_base
            
            resultados[juego] = f"{fps} FPS"
            
        return resultados
    
    def realizar_informe_uso(self):
        
        informe = super().realizar_informe_uso()
        informe.update({
            "Tipo" : "Gaming",
            "Uso Recomendado":"Juegos de video",
            "Horas de uso" : 10,
            "Recomendaciones de software" : ["Antivirus", "VPN"]            
        })
    
        return informe
    

