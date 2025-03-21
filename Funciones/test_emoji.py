import Funciones.emoji as emoji

cantida_frase = int(input("Cuantas frases desea ingresar: "))

for i in range(cantida_frase):
    frase = input("ingrese la frase:")
    emoji.econtrar_palabra(frase)
    emoji.agregar_frase(frase)