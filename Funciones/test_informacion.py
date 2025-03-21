import Funciones.informacion as informacion

for i in range(13):
    nombre  = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    fecha_nacimiento = int(input("ingresa la fecha de nacimiento: "))
    
    informacion.agregar_nombre(nombre,apellido)
    informacion.agregar_edad(fecha_nacimiento)
    

print(informacion.nombre_paciente)
print(informacion.edades)

indice_mayor = informacion.edades.index(max(informacion.edades))
indice_menor = informacion.edades.index(min(informacion.edades))

nombre_mayor = informacion.nombre_paciente[indice_mayor]
nombre_menor = informacion.nombre_paciente[indice_menor]

print(f"El paciente con mayor edad es: {nombre_mayor} con la edad de: {max(informacion.edades)}" )
print(f"El paciente con menor edad es: {nombre_menor} con la edad de: {min(informacion.edades)}" )

