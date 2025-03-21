menu =["Seco de pollo", "Sopa de Carne", "Encebollado", "Papas Fritas", "Caldo de Pata"]

nuevoPlato = input("Ingrese el nombre del nuevo platillo: ")

menu.append(nuevoPlato)

print(f"El nuevo plato: {nuevoPlato} fue agregado con exito")

dato_buscar= input("Ingrese el nombre del plantillo a buscar: ")

encontrado = dato_buscar in menu

if encontrado:
    print("El plantillo fue encontrado en la posicion: ", menu.index(dato_buscar), " coincidencias con ese nombre: ", menu.count(dato_buscar))
    
    
else:
    print("No existe un platillo con ese nombre")
    
dato_eliminar = input("Ingrese el nombre del platillo que desea eliminar: ")

menu.remove(dato_eliminar)

print("Platillo eliminado con exito")

print(f"Menu actual: {menu}")