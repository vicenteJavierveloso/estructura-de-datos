estudiantes = {"nombres_estudiantes": [],
               "nombre_asignatura": "",
               "notalab1": 0,
               "notalab2": 0}
print(f"Ingrese el nombre de los estudiantes ")
for i in range(3):
    estudiantes["nombres_estudiantes"].append(input())
print(f"Ingresar nombre de la asignatura ")
estudiantes["nombre_asignatura"] = input()
print(f"Ingresar nota laboratorio 1 ")
estudiantes["notalab1"] = float(input())
print(f"Ingresar nota laboratorio 2 ")
estudiantes["notalab2"] = float(input())
print(estudiantes)
promedio = (estudiantes["notalab1"]*0.3)+(estudiantes["notalab2"]*0.7)
print(f"Promedio: {promedio:.1f}")