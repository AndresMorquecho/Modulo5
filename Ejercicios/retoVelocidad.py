import random

(message_min) = "La velocidad a la que se esta conduciendo es inferior al permitido"
(message_max) = "La velocidad a la que se esta conduciendo es supeior al permitido, reduzca la velocidad inmediatamente"
(message_nor) = "La velocidad a la que se esta conduciendo es la adecuada"


pais = input("Elige el pais (Ecuador, Colombia, Peru): ").capitalize()
zona = input("Ingrese la zona en la cual esta viajando (Urbana, Rural o Perimetral) ").capitalize()
velocidad = float(input("ingrese la velocidad a la cual esta conduciendo "))


if pais == "Ecuador":
    if zona == "Urbana":
        if velocidad < 10:
            print(message_min)
        elif velocidad >50:
            print(message_max)
        else:
            print(message_nor)
    elif zona == "Rural":
        if velocidad < 51:
            print(message_min)
        elif velocidad >70:
            print(message_max)
        else:
            print(message_nor)
    else:
        if velocidad < 71:
            print(message_min)
        elif velocidad >90:
            print(message_max)
        else:
            print(message_nor)  
elif pais == "Peru":
    if zona == "Urbana":
        if velocidad < 10:
            print(message_min)
        elif velocidad >40:
            print(message_max)
        else:
            print(message_nor)
    elif zona == "Rural":
        if velocidad < 41:
            print(message_min)
        elif velocidad >60:
            print(message_max)
        else:
            print(message_nor)
    else:
        if velocidad < 61:
            print(message_min)
        elif velocidad >120:
            print(message_max)
        else:
            print(message_nor)
else:
    if zona == "Urbana":
        if velocidad < 10:
            print(message_min)
        elif velocidad >30:
            print(message_max)
        else:
            print(message_nor)
    elif zona == "Rural":
        if velocidad < 31:
            print(message_min)
        elif velocidad >80:
            print(message_max)
        else:
            print(message_nor)
    else:
        if velocidad < 81:
            print(message_min)
        elif velocidad >100:
            print(message_max)
        else:
            print(message_nor)    

 
        

        
    