from Libro import Libro

El_Quijote = Libro("El Quijote de la Mancha", "Migue de Cervantes,", 400)
Cien_anios_soledad = Libro("Cien años de Soledad", "Gabriel Carcia Maquez",200)
Harry_potter = Libro("Harry Potter","J.K",400)


Libro.mostrar_info(El_Quijote)
Libro.mostrar_info(Cien_anios_soledad)
Libro.mostrar_info(Harry_potter)

if Libro.es_grande(El_Quijote.paginas):
     print(f"El libro {El_Quijote.titulo} es grande con un total de {El_Quijote.paginas} páginas ")
     
print(f"N° de Libros creado hasta el momento: {Libro.cantidad_libros()} " )