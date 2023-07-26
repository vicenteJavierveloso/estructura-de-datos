#Multiplicacion de matrices usando listas
import random
n1 = int(input("Filas matriz 1 "))
m1 = int(input("Columnas matriz 1 "))

n2 = int(input("Filas matriz 2 "))
m2 = int(input("Columnas matriz 2 "))

if m1 == n2:
    pass
else:
    print("No se pueden multiplicar matrices del orden proporcionado")
    exit()

matriz1 = []
matriz2 = []

#Llenar matriz1
for i in range(n1):
    aux = []
    for j in range(m1):
        aux.append(random.randint(0,5))
    matriz1.append(aux)

#Llenar matriz2
for i in range(n2):
    aux = []
    for j in range(m2):
        aux.append(random.randint(0,5))
    matriz2.append(aux)

print(f"Matriz 1 \n{matriz1}")
print(f"Matriz 2 \n{matriz2}")

#Creacion de matriz3 con el resultado de la multiplicacion (n1xm2)
matriz3 = []
for i in range(n1):
    aux = []
    for j in range(m2):
        aux.append(0)
    matriz3.append(aux)
#Aun no multiplica