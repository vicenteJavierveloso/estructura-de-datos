import random
n1 = int(input("Filas matriz 1 "))
m1 = int(input("Columnas matriz 1 "))

matriz1 = []
for i in range(n1):
    aux = []
    for j in range(m1):
        aux.append(random.randint(0,5))
    matriz1.append(aux)

n2 = int(input("Filas matriz 2 "))
m2 = int(input("Columnas matriz 2 "))
matriz2 = []
for i in range(n2):
    aux = []
    for j in range(m2):
        aux.append(random.randint(0,5))
    matriz2.append(aux)

print(matriz1)
print(matriz2)

def suma(a,b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        return "No se pueden sumar matrices de distinto tamaño."
    else:
        for i in range(len(a)):
            for j in range(len(a[0])):
                a[i][j] = a[i][j]+b[i][j]
        return a

def resta(a,b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        return "No se pueden restar matrices de distinto tamaño."
    else:
        for i in range(len(a)):
            for j in range(len(a[0])):
                a[i][j] = a[i][j]-b[i][j]
        return a
    
print(suma(matriz1,matriz2))
print(resta(matriz1,matriz2))