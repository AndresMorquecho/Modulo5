class Libro:
    
    contador_libros = 0
    
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

        Libro.contador_libros +=1
    
    def mostrar_info(self):
        print(f"Titulo: {self.titulo} Autor: {self.autor} Número Páginas: {self.paginas}")
        
    @staticmethod
    def es_grande(paginas):
        if paginas > 300:
            return True
        else:
            return False
    
    @classmethod
    def cantidad_libros(cls):
        return cls.contador_libros