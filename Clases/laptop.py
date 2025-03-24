class Laptop:
    def __init__(self, marca, procesado, memoria, costo = 500, impuesto = 10):
        self.marca = marca
        self.procesado = procesado
        self.memoria = memoria
        self.costo = costo
        self.impuesto = impuesto
        

    def valor_final(self):
        return self.costo  + self.impuesto

    def valor_descuento(self, descuento):
        return (self.costo * descuento)/ 100
    
    
    #Metodos estaticos
    
    @staticmethod
    def comparar_costo(laptop1, laptop2):
            if laptop1.costo == laptop2.costo:
                print(f"El costo de la laptop {laptop1.marca} es igual a de la laptop {laptop2.marca}")
            else:
                print("Los costos de la laptos no son los mismos")

    #Metodo de clase
    
    @classmethod
    def asus_laptop(cls, costo): #cls es la referencia a la propia clase
        marca = "asus"
        procesado = "I5"
        memoria = 16
        return cls(marca, procesado, memoria,costo)
    