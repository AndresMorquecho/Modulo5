from Vehiculos import Vehiculo

class Moto(Vehiculo):
    def __init__(self, marca, modelo, anio, tipo):
        super().__init__(marca, modelo, anio)
        self.tipo = tipo
    
    def descripcion(self):
        print(f" Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio} Numero Puertas: {self.tipo} ")
        