import numpy as np

n1 = int(input("Filas matriz 1 "))
m1 = int(input("Columnas matriz 1 "))

n2 = int(input("Filas matriz 2 "))
m2 = int(input("Columnas matriz 2 "))

matriz1 = np.zeros((n1,m1))
matriz2 = np.zeros((n2,m2))

#Llenar matriz 1
for i in range(n1):
    for j in range(m1):
        matriz1[i][j] = float(input(f"Elemento {i,j} matriz 1 "))

#Llenar matriz 2
for i in range(n2):
    for j in range(m2):
        matriz2[i][j] = float(input(f"Elemento {i,j} matriz 2 "))

print(matriz1)
print(matriz2)
#Suma
suma = np.add(matriz1,matriz2)
#Resta
resta = np.subtract(matriz1,matriz2)
print(suma)
print(resta)