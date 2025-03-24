import reto
mi_auto = reto.auto("Chevrolet", "Picanto", 2018)
tu_auto = reto.auto("Mazda","evo", 2012)


print(reto.auto.comparar_kilometraje(mi_auto, tu_auto))
print(reto.auto.esAutoClasico(tu_auto))

#Métodos de Clase
auto_economico = reto.auto.crear_auto_economico()
print(auto_economico.__dict__)

auto_premiun = reto.auto.crear_auto_premium()
print(auto_premiun.__dict__)