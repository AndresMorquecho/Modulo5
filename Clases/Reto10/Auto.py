
from Vehiculos import Vehiculo

class Auto(Vehiculo):
    def __init__(self, marca, modelo, anio, numero_puertas):
        super().__init__(marca, modelo, anio)
        self.numero_puertas = numero_puertas
    
    def descripcion(self):
        print(f" Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio} Numero Puertas: {self.numero_puertas} ")
                
