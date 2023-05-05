#Multiplicacion de matrices utilizando numpy
import numpy as np
import random

n1 = int(input("Filas matriz 1 "))
m1 = int(input("Columnas matriz 2 "))

n2 = int(input("Filas matriz 2 "))
m2 = int(input("Columnas matriz 2 "))

#Comprueba si las matrices se pueden multiplicar
if m1 == n2:
    pass
else:
    #Sale del programa si las matrices a ingresar no son del orden apropiado para multiplicar
    print("Las matrices no pueden ser multiplicadas")
    exit()

matriz1 = np.zeros((n1,m1))
matriz2 = np.zeros((n2,m2))

#Llenar matriz 1
for i in range(n1):
    for j in range(m1):
        matriz1[i][j] = random.randint(0,5)
#Llenar matriz 2
for i in range(n2):
    for j in range(m2):
        matriz2[i][j] = random.randint(0,5)

print(f"Matriz 1 \n{matriz1}")
print(f"Matriz 2 \n{matriz2}")

#Metodo __matmul__ permite multiplicar dos matrices que sean del orden apropiado
print(f"Multiplicacion \n{matriz1.__matmul__(matriz2)}")