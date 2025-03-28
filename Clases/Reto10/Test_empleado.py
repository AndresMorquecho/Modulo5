from EmpleadoMedioTiempo import Empleado_Medio_Tiempo
from EmpleadoTiempoCompleto import EmpleadoTimepoCompleto
Roberto_HalfTime = Empleado_Medio_Tiempo("Robeto", 200, 10) 
Juan_Fulltime = EmpleadoTimepoCompleto("Juan", 400, 20)
Empleados_List = [
    EmpleadoTimepoCompleto("Juan", 400, 20),
    Empleado_Medio_Tiempo("Roberto", 200, 10),
    EmpleadoTimepoCompleto("Maria", 450, 22),
    EmpleadoTimepoCompleto("Carlos", 420, 25),
    EmpleadoTimepoCompleto("Luisa", 430, 24),
    EmpleadoTimepoCompleto("Pablo", 410, 21),
    EmpleadoTimepoCompleto("Ana", 400, 20),
]
for item in Empleados_List:
    print(f" El salario final más bonos del Empleado {item.nombre} es de:  ${item.calcular_salario()}")
    