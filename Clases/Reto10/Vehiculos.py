class Vehiculo:
        def __init__(self, marca, modelo, anio):
            
            self.marca = marca
            self.modelo = modelo
            self.anio = anio


        def descripcion(self):
            print(f" Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio} ")
        