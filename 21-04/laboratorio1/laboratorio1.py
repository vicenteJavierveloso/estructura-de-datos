import numpy as np
import random

#Creacion de matriz 1
filas = int(input("Ingrese numero de filas para matriz 1 "))
columnas = int(input("Ingrese numero de columnas para matriz 1 "))

matriz1 = np.zeros((filas,columnas))

for i in range(filas):
    for j in range(columnas):
        matriz1[i][j] = random.randint(0,5)

print(f"Matriz 1\n{matriz1}")

#Creacion de matriz 2
filas2 = int(input("Ingrese numero de filas para matriz 2 "))
columnas2 = int(input("Ingrese numero de columnas para matriz 2 "))

matriz2 = np.zeros((filas2,columnas2))

for i in range(filas2):
    for j in range(columnas2):
        matriz2[i][j] = random.randint(0,5)

print(f"Matriz 2\n{matriz2}")

#Suma de matrices 
#Se intenta sumar las matrices, si no es posible se da aviso al usuario
try:
    suma_matrices = matriz1 + matriz2
except:
    print(f"Las matrices no pueden ser sumadas")
    exit()

print(f"Suma de matrices\n{suma_matrices}")

#Creacion de matriz 3

filas3 = int(input("Ingrese numero de filas para matriz 3 "))
columnas3 = int(input("Ingrese numero de columnas para matriz 3 "))
matriz3 = np.zeros((filas3, columnas3))

for i in range(filas3):
    for j in range(columnas3):
        matriz3[i][j] = random.randint(0,5)

print(f"Matriz 3\n{matriz3}")

#Resta entre la suma de matrices 1 y 2 y la matriz 3
#Intenta restar las matrices si no es posible se lanza un error al usuario
try:
    resta_matrices = matriz3 - suma_matrices
except:
    print(f"Las matrices no pueden ser restadas")
    exit()

print(f"Resta entre la suma de matrices anteriores y la matriz 3\n{resta_matrices}")
