from array import array
import random

arreglo = array('f', [0,0,0,0,0,0,0,0,0,0])
tamano = random.randint(10,30)
for i in range(tamano):
    arreglo.append(0)
for i in range(len(arreglo)):
    arreglo[i] = random.randint(0,9)

print(arreglo)

buscar = int(input("Elemento a buscar "))

contador = 0
indices = []
for i in range(len(arreglo)):
    if arreglo[i] == buscar:
        contador += 1
        indices.append(i)
print(f"El elemento aparece {contador} veces, en los indices {indices}")
