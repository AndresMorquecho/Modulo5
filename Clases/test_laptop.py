from laptop import Laptop
    
Laptop_pepito = Laptop("Lenovo","i7",32)
Laptop_Maria = Laptop("Dell","i5", 32)



for numero in range(1,1001):    
    asus_laptop = Laptop.asus_laptop(numero)
    print(asus_laptop.__dict__)


# Laptop.comparar_costo(Laptop_Maria, Laptop_pepito)
