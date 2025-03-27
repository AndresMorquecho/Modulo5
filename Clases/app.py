from laptop_gaming import laptop_gaming
import tkinter as tk #modulo para construir interface graficas as tk es un alias para poder llamar al tkinter
from tkinter import ttk # team tk inter
from PIL import Image, ImageTk
import random


class App:
    def __init__(self,root):
        self.root = root
        self.laptops = []
        self.imagenes = ["C:\\Users\\Estudio\\Desktop\\Modulo5\\Clases\\Images_laptop\\20200824120814.jpg",
                        "C:\\Users\\Estudio\\Desktop\\Modulo5\\Clases\\Images_laptop\\images (3).jpg",
                        "C:\\Users\\Estudio\\Desktop\\Modulo5\\Clases\\Images_laptop\\imsdfages (3).jpg",
                        "C:\\Users\Estudio\\Desktop\\Modulo5\\Clases\\Images_laptop\\imsdfsasages (3).jpg",
                        "C:\\Users\\Estudio\\Desktop\\Modulo5\\Clases\\Images_laptop\\imssages (3).jpg"]
        

        root.title("Ingresar Datos")
        self.setup_ui()
        
    def guardar_laptop(self):
        
        nueva_laptop = laptop_gaming(self.marca.get(),self.procesador.get(),self.memoria.get(), self.tarj_grafica.get())
        
        self.laptops.append(nueva_laptop)
        self.mostrar_laptops.insert(tk.END, f"{nueva_laptop}")
        
        self.mostrar_imagenes_aleatorias()
        
    def mostrar_imagenes_aleatorias(self):
        imagen_path = random.choice(self.imagenes)
        imagen = Image.open(imagen_path)
        imagen = imagen.resize((200,200), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(imagen)
        
        self.canva.create_image(0,0, anchor =  tk.NW, image = photo)
        self.canva.image = photo
        
        
        pass

    def setup_ui(self):
        
        ttk.Label(self.root, text="Marca").grid(row=0, column=0) # pide dos parametros donde va a estar ubicado y luego el caption del label
        self.marca =  tk.StringVar()                
        ttk.Entry(self.root, textvariable=self.marca).grid(row=0, column=1)
        
        
        ttk.Label(self.root, text="Procesador").grid(row=1, column=0) # pide dos parametros donde va a estar ubicado y luego el caption del label
        self.procesador =  tk.StringVar()                
        ttk.Entry(self.root, textvariable=self.procesador).grid(row=1, column=1)
        
        
        ttk.Label(self.root, text="Memoria").grid(row=2, column=0) # pide dos parametros donde va a estar ubicado y luego el caption del label
        self.memoria =  tk.StringVar()                
        ttk.Entry(self.root, textvariable=self.memoria).grid(row=2, column=1)
        
        
        ttk.Label(self.root, text="Tarjeta Gráfica").grid(row=3, column=0) # pide dos parametros donde va a estar ubicado y luego el caption del label
        self.tarj_grafica =  tk.StringVar()                
        ttk.Entry(self.root, textvariable=self.tarj_grafica).grid(row=3, column=1)
        
        
        ttk.Label(self.root, text="Precio").grid(row=4, column=0) # pide dos parametros donde va a estar ubicado y luego el caption del label
        self.precio =  tk.StringVar()                
        ttk.Entry(self.root, textvariable=self.precio).grid(row=4, column=1)
        
        
        ttk.Button(self.root,text="Agregar Laptop",command=self.guardar_laptop).grid(row=5, column=0)
        
        self.mostrar_laptops = tk.Text(self.root, height=10, width=50)
        self.mostrar_laptops.grid(row=6, column=0, columnspan=2)

        self.canva = tk.Canvas(self.root, width=200, height=200)
        self.canva.grid(row=1, column=3, rowspan=6)      



root = tk.Tk() # construyo mi ventana
app = App(root) # se crea la instancia y se pasa la ventana que se crea
root.mainloop() # metodo que puedo oir todos los eventos que sucedene en mi ventana





