class auto:
    def __init__(self, marca, modelo, año, kilometraje = 0):
        self.marca = marca
        self.modelo = modelo
        self.año =año
        self.kilometraje = kilometraje
        
    def mostrar_informacion(self):
        print(self.marca, self.modelo, self.año)
            
    def actualizar_kilometraje(self,nuevo_kilometraje):
        if nuevo_kilometraje < self.kilometraje:
                print(f" El kilometraje ingresado: {nuevo_kilometraje} es menor al actual {self.kilometraje}. No se puede reducir el kilometraje")
        else:
            self.kilometraje = nuevo_kilometraje
            
    def realizar_viaje(self,kilometros):
        if kilometros < 0:
            print("La cantidad de kilometraje debe ser positiva")
        else:
            self.kilometraje += kilometros
    def estado_auto(self):
        if self.kilometraje < 20000:
            print(f"Estoy como nuevo con: {self.kilometraje} km")
        elif self.kilometraje >=20000 and self.kilometraje <= 100000:
            print(f"Ya estoy usado: {self.kilometraje} km")
        elif self.kilometraje >100000:
            print(f" Y déjame descansar por favor !!!!  {self.kilometraje} km")
            
    @staticmethod
    def comparar_kilometraje(auto1, auto2):
        if auto1.kilometraje == auto2.kilometraje:
            return(f"el kilometraje del auto {auto1.marca} ({auto1.kilometraje}) es igual al kilometraje del auto {auto2.marca} ({auto2.kilometraje})")
        else:
            return(f"el kilometraje del auto {auto1.marca} ({auto1.kilometraje}) no es igual al kilometraje del auto {auto2.marca} ({auto2.kilometraje})")
    
    @staticmethod
    def esAutoClasico(auto):
        if auto.año < 2004:
            return (f"El auto {auto.marca} es considera clasico")
        else:
            return (f"El auto {auto.marca} no es considera clasico")
     
            
    @classmethod
    def crear_auto_economico(cls):
        return cls(marca = "Generico", modelo = "Eco-2025", año = 2025) 
    
    @classmethod
    def crear_auto_premium(cls):
        return cls(marca = "Premiun", modelo = "Alta-gama", año = 2025)       
                    
        
        

    