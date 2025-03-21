cantidad_Datos = int(input("ingresa la cantidad de datos a ingresar (1,2,3 ...) "))
datos = []

for i in range(cantidad_Datos):
    dato_nuevo = input("ingrese el dato: ")
    
    if dato_nuevo.isalpha():
        datos.append(dato_nuevo)
    else:
        try:
            decimal = float(dato_nuevo)
            datos.append(decimal)
        except ValueError:
            print("El dato no es texto ni decimal")

print(f"Su lista es {datos}")            