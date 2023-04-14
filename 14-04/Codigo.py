import random
arreglo = [3,2,4,1]
arreglo.sort()
arreglo.reverse()
print(arreglo)

#Usando un metodo del modulo random
#random.shuffle(lista)

for i in range(len(arreglo)):
    aux=0
    r=random.randint(0, len(arreglo)-1)
    #Guarda el elemento en la posicion i
    aux=arreglo[i]
    #Cambia el elemento de la posicion i por alguno aleatorio en otra posicion
    arreglo[i]=arreglo[r]
    #Como se guardo el elemento que se acaba de modificar, se intercambia con el objeto
    #En la posicion aleatoria
    arreglo[r]=aux
print(arreglo)

nombre_rut= []
for i in range(5):
    persona = [input("Nombre "),input("Rut ")]
    nombre_rut.append(persona)

print(nombre_rut)
nombre_rut.sort()
print(nombre_rut)