import numpy as np
import random

#Creacion de matriz 1
filas = int(input("Ingrese numero de filas para la matriz "))
columnas = int(input("Ingrese numero de columnas para la matriz "))
escalar = int(input("Ingrese un escalar para multiplicar la matriz "))

matriz = np.zeros((filas,columnas))

for i in range(filas):
    for j in range(columnas):
        matriz[i][j] = random.randint(0,10)

print(f"Matriz 1\n{matriz}")
print(f"Matriz por escalar\n{escalar*matriz}")

