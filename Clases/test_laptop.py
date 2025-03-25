from laptop import Laptop
from laptop_gaming import laptop_gaming
from laptop_business import Laptop_business
    
Laptop_pepito = Laptop("Lenovo","i7",32)
Laptop_Maria = Laptop("Dell","i5", 32)
laptop_rtx = laptop_gaming("Asus","i7",4,"RTX 8GB")


# for numero in range(1,1001):    
#     asus_laptop = Laptop.asus_laptop(numero)
#     print(asus_laptop.__dict__)


#print(laptop_rtx.realizar_diagnostico_sistema())

# Laptop.comparar_costo(Laptop_Maria, Laptop_pepito)

laptop_empresarial = Laptop_business("Dell","intel i7",16, "SSD 1 TB", 4)

print(laptop_empresarial.realizar_diagnostico_sistema())