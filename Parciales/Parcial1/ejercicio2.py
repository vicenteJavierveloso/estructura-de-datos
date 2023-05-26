#Vicente Javier Veloso Gomez
from ejercicio1 import llenar_matriz
from ejercicio1 import matriz_a_str
import numpy as np

A = []
B = []
C = []

llenar_matriz(A,3,3,1,10)
llenar_matriz(B,3,3,11,30)
llenar_matriz(C,3,3,-10,-1)

print(f"Matriz 1: \n{matriz_a_str(A)}\nMatriz 2: \n{matriz_a_str(B)}\nMatriz 3: \n{matriz_a_str(C)}")

#Resultado de (A+B) * C
if np.shape(A) == np.shape(B):
    if np.shape(np.add(A,B))[1] == np.shape(C)[0]:
        resultado_1 = np.dot(np.add(A,B),C)
        print(f"Resultado de (A+B)*C: \n{resultado_1}")
    else:
        print(f"Las matrices no pueden ser multiplicadas")
else:
    print(f"Las matrices no pueden ser sumadas")

#Resultado de A*C + B*C
if np.shape(A)[1] == np.shape(C)[0]:
    if np.shape(B)[1] == np.shape(C)[0]:
        if np.shape(np.dot(A,C)) == np.shape(np.dot(B,C)):
            resultado_2 = np.add(np.dot(A,C), np.dot(B,C))
            print(f"Resultado de A*C + B*C: \n{resultado_2}")
        else:
            print(f"A*C y B*C no pueden ser sumadas")
    else:
        print(f"B y C no pueden ser multiplicadas")
else:
    print(f"A y C no pueden ser multiplicadas")
