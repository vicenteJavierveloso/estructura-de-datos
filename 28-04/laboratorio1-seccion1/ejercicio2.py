import random
import operator
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

print(f"1 {matriz1}")
print(f"2 {matriz2}")

def suma(a,b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        return "No se pueden sumar matrices de distinto tamaño."
    else:
        for i in range(len(a)):
            for j in range(len(a[0])):
                a[i][j] = a[i][j]+b[i][j]
        return a

def resta(c,d):
    if len(c) != len(d) or len(c[0]) != len(d[0]):
        return "No se pueden restar matrices de distinto tamaño."
    else:
        matriz3 = []
        for i in range(len(c)):
            aux = []
            for j in range(len(c[0])):
                o = c[i][j]
                p = d[i][j]
                aux.append(operator.sub(o,p))
            matriz3.append(aux)
        # for i in range(len(c)):
        #     for j in range(len(c[0])):
        #         aux = c[i][j] - d[i][j]
        #         matriz3[i][j] = aux
        return matriz3
    
print(suma(matriz1,matriz2))
#La resta no funciona
print(resta(matriz1,matriz2))