planetas = ["Mercurio", "Venus", "Tierra", "Marte","Jupiter","Saturno","Urano","Neptuno"]

# print(f"Los planetas son:  {planetas[-1]}")
# print(f"Los planetas son:  {planetas[2: ]}")
# print(len(planetas))

gravedad_Planetas = [0.378, 0.78, 1, 0.377, 0.912, 0.889, 1.22]
peso_bus = 12323

# print(f"En la tierra, un autobus de dos pisos pesa {peso_bus} N")
# print(f"En la Mercurio, un autobus de dos pisos pesa {peso_bus * gravedad_Planetas[0]} N")

print(f"Lo mas liviano que sería un autobús en el sistema solar es {peso_bus * min(gravedad_Planetas)}")
print(f"Lo mas pesado que sería un autobús en el sistema solar es {peso_bus * max(gravedad_Planetas)}")