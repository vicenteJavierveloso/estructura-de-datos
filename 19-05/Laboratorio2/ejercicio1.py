#Vicente Javier Veloso Gomez
import random as ran
import numpy as np

n = ran.randint(2,5)
m = ran.randint(2,5)

matriz1 = []
matriz2 = []
for i in range(n):
    aux = []
    for j in range(m):
        aux.append(int(input(f"Ingrese elemento {i},{j} para la matriz 1 ")))
    matriz1.append(aux)
for i in range(n):
    aux = []
    for j in range(m):
        aux.append(int(input(f"Ingrese elemento {i},{j} para la matriz 2 ")))
    matriz2.append(aux)

print(f"Matriz 1 = \n{matriz1}")
print(f"Matriz 2 = \n{matriz2}")

#Resta de matrices

def resta_matrices(a,b):
    filas_a = len(a)
    columnas_a = len(a[0])
    filas_b = len(b)
    columnas_b = len(b[0])
    #Verificar si se puede
    if filas_a == filas_b and columnas_a == columnas_b:
        for i in range(filas_a):
            for j in range(columnas_a):
                a[i][j] = a[i][j]-b[i][j]
        return a
    else:
        return None

matriz_resultante = resta_matrices(matriz1,matriz2)
print(f"Matriz resultante de la resta = \n{matriz_resultante}")

#Crea una nueva matriz 3 con la cual multiplicar 
matriz3 = []
n3 = int(input(f"Filas de la nueva matriz 3 "))
m3 = int(input(f"Columnas de la nueva matriz 3 "))
for i in range(n3):
    aux = []
    for j in range(m3):
        aux.append(int(input(f"Elemento {i}{j} para la nueva matriz ")))
    matriz3.append(aux)

print(f"Matriz 3 = \n{matriz3}")

#Usando numpy convierte las listas en arrays que pueda trabajar
matriz_resultante = np.array(matriz_resultante,dtype=float)
matriz3= np.array(matriz3,dtype=float)
if matriz_resultante.shape[1]==matriz3.shape[0]:
    producto = np.matmul(matriz_resultante,matriz3)
    print(f"Producto entre la resta de las matrices 1 y 2, y la matriz 3 = \n {producto}")
else:
    print("No se pueden multiplicar las matrices ingresadas")

print("Demostracion de propiedad (A*B)^t = B^t*A^t")
#Demostracion de propiedad matrices traspuestas
#Crear matrices que sean multiplicables con elementos aleatorios

A = np.zeros((4,2))
B = np.zeros((2,3))

for i in range(4):
    for j in range(2):
        A[i][j] = ran.randint(0,10)
for i in range(2):
    for j in range(3):
        B[i][j] = ran.randint(0,10)


AB = np.matmul(A,B)

ABt = np.transpose(AB)

Bt = np.transpose(B)
At = np.transpose(A)

BtAt = np.matmul(Bt,At)

print(f"A = \n{A}")
print(f"B = \n{B}")
print(f"(A*B)^t = \n{ABt}")
print(f"B^t = \n{Bt}")
print(f"A^t = \n{At}")
print(f"B^t*A^t = \n{BtAt}")


