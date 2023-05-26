#Vicente Javier Veloso Gomez
import random as ran
import numpy as np

def llenar_matriz(matriz:list,filas:int,columnas:int,a:int,b:int):
    for i in range(filas):
        aux = []
        for j in range(columnas):
            aux.append(ran.randint(a,b))
        matriz.append(aux)

def matriz_a_str(matriz:list):
    aux = ""
    for i in range(len(matriz)):
        aux += str(matriz[i]) + "\n"
    return aux

#Crear tres matrices
A = []
B = []
C = []

llenar_matriz(A,4,4,0,10)
llenar_matriz(B,4,4,0,10)
llenar_matriz(C,4,4,0,10)

#MOstrar matrices generadas
print(f"Matriz A: \n{matriz_a_str(A)}\nMatriz B: \n{matriz_a_str(B)}\nMatriz C: \n{matriz_a_str(C)}")

# verificar que se pueden calcular inversas de las matrices generadas
# usando determinante != 0
#Verificar si las matrices se pueden multiplicar
#A*A
if np.shape(A)[1] == np.shape(A)[0]:
    #A^2*A
    if np.shape(np.dot(A,A))[1] == np.shape(A)[0]:
        #determinante de B para inversa
        if np.linalg.det(B) != 0:
            #ver si A^3 es multiplicable con inversa de B
            if np.shape(np.dot(np.dot(A,A),A))[1] == np.shape(np.invert(B))[0]:
                #Si A^3*B^-1 es multiplicable con C
                if np.shape(np.dot(np.dot(np.dot(A,A),A),np.invert(B)))[1] == np.shape(C)[0]:
                    #determinante de A^3 para inversa
                    if np.linalg.det(np.dot(np.dot(A,A),A)) != 0:
                        if np.shape(np.dot(np.dot(np.dot(np.dot(A,A),A),np.invert(B)),C)) == np.shape(np.invert(np.dot(np.dot(A,A),A))):
                            #Resultado de (A^3*B^-1*C) + (A^3)^-1
                            resultado = np.add(np.dot(np.dot(np.dot(np.dot(A,A),A),np.invert(B)),C), np.invert(np.dot(np.dot(A,A),A)))
                        else:
                            print(f"A^3*B^-1*C no puede ser sumado con (A^3)^-1")
                    else:
                        print(f"La matriz A^3 no puede tener inversa (determinante)")
                else:
                    print(f"A^3*B^-1 no puede multiplicarse con C")
            else:
                print(f"A^3 no se puede multiplicar con la inversa de B")
        else:
            print(f"La matriz B no puede tener inversa (determinante)")
    else:
        print(f"A^2 no puede multiplicarse con A")
else:
    print(f"A no puede multiplicarse con A")

print(f"Matriz resultado de (A^3*B^-1*C) + (A^3)^-1: \n{resultado}")