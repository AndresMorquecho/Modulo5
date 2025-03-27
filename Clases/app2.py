from laptop_business import Laptop_business
import random
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk

class App:
    def __init__(self, root):
        self.root = root
        self.laptops = []
        self.imagenes =  ["C:\\Users\\Estudio\\Desktop\\Modulo5\\Clases\\Images_laptop\\20200824120814.jpg",
                        "C:\\Users\\Estudio\\Desktop\\Modulo5\\Clases\\Images_laptop\\images (3).jpg",
                        "C:\\Users\\Estudio\\Desktop\\Modulo5\\Clases\\Images_laptop\\imsdfages (3).jpg",
                        "C:\\Users\Estudio\\Desktop\\Modulo5\\Clases\\Images_laptop\\imsdfsasages (3).jpg",
                        "C:\\Users\\Estudio\\Desktop\\Modulo5\\Clases\\Images_laptop\\imssages (3).jpg"]
        
        root.title("Ingreso de laptops")
        self.setup_ui()
        pass
    
    def agregar_laptop(self):
        
        nueva = Laptop_business(self.marca.get(), self.procesador.get(),
                                self.memoria.get(), self.almacenamiento.get(), self.duracion_bat.get()
                                )
        
        self.laptops.append(nueva)
        
        self.mostrar_lap.insert(tk.END, f"{nueva}")
        
        self.motrar_image()
        
        
        pass
    def motrar_image(self):
        image_path = random.choice(self.imagenes)
        imagen = Image.open(image_path)
        imagen = imagen.resize((100,100), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(imagen)
        
        self.canvaImage.create_image(0,0, anchor = tk.NW, image = photo)
        self.canvaImage.image = photo
        
    
    def setup_ui(self):
        ttk.Label(self.root, text="Marca").grid(row=0 , column=0)
        self.marca = tk.StringVar()
        ttk.Entry(self.root, textvariable= self.marca).grid(row=0, column=1)
        
        
        ttk.Label(self.root, text="Procesador").grid(row = 1, column=0)
        self.procesador = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.procesador).grid(row=1, column=1)
        
        ttk.Label(self.root, text="Memoria").grid(row=2, column=0)
        self.memoria = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.memoria).grid(row=2  ,column=1)
        
        ttk.Label(self.root, text="Almacenamiento").grid(row=3, column=0)
        self.almacenamiento = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.almacenamiento).grid(row= 3, column=1)
        
        ttk.Label(self.root, text="Duracion Bateria").grid(row = 4, column=0)
        self.duracion_bat = tk.StringVar()
        ttk.Entry(self.root, textvariable= self.duracion_bat).grid(row=4, column=1)
        
        self.mostrar_lap = tk.Text(self.root, height=7, width=50)
        self.mostrar_lap.grid(row=2, column=3, rowspan=3)
        
        ttk.Button(self.root, text="Agregar Laptop", command=self.agregar_laptop).grid(row=6, column= 0, columnspan=2)
        
        self.canvaImage = tk.Canvas(self.root, width=100 ,height=100)
        self.canvaImage.grid(row=0, column=3, rowspan=2)
        
        
        pass
        
root = tk.Tk() #form o ventana
app = App(root)
root.mainloop()

