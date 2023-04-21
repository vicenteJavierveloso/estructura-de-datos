from array import array
import random

matriz = []
for i in range(5):
    matriz.append(array('f', [0,0,0,0,0]))

for i in range(len(matriz)):
    for o in range(len(matriz[0])):
        matriz[i][o] = random.randint(0,5)

print(matriz)

buscar_fila = int(input("Fila a buscar "))
buscar_columna = int(input("Columna a buscar "))

print(f"El elemento es {matriz[buscar_fila-1][buscar_columna-1]}")