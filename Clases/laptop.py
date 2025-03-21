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
    
    

Laptop_pepito = Laptop("Lenovo","i7",32)



print(Laptop_pepito.__dict__)
print(Laptop_pepito.valor_final())
print(f" el valor del descueto es: {Laptop_pepito.valor_descuento(10)}")
