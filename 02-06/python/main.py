newtupla = tuple()
grupo1 = ("Daniel", "Cristian", "Felipe",200,100,"Daniel")
print("##Tuplas##")
print(type(grupo1))

#Accediendo al primer elemento de la tupla
print(grupo1[0])

#Consultando el elemento que se repite
print("El elemento se repite,", grupo1.count("Daniel"))
#Index muestra la primera ocurrencia del elemento
print("Indice del elemento,", grupo1.index("Daniel"))

#Reasignando el primer elemento de la tupla
# grupo1[0] = "Constanza"
# print(grupo1)

grupo2 = ("Pedro", 100, "Felipe", "Diego")

#Sets
conjunto_vacio = set()
conjunto_vacio1 = {} # -> Diccionario
print(type(conjunto_vacio1))

conjunto_colores = set({"Azul","Rojo","Verde"})
conjunto_animales = {"Gato","Perro","Pajaro"}

print("El primer set contiene los siguientes colores", conjunto_colores)
print("El segundo set contien los siguientes animales", conjunto_animales)
# conjunto_colores.add("Celeste")

datos_personales = {
    "nombre": "victor",
    "institucion": "ulagos",
    "edad": 29
}

print(datos_personales)
#
#se anidan un diccionario y un set
datos_personales = {
    "nombre": "victor",
    "institucion": "ulagos",
    "edad": 29,
    "asignaturas": {"Estructura de datos", "Programacion"}
}

#Se puede consultar la longitud del diccionario
print(len(datos_personales))

print(datos_personales["institucion"])

#modificar el valor de una clave
datos_personales["institucion"] = "USS"
print("Diccionario actualizado", datos_personales)

#agregandouna nueva clave
datos_personales["ciudad"] = "Osorno"
#se añade clave y valor

hospital = dict(
    nombre = "Hospital san jose",
    direccion = "dr. guillermo buhler 1765",
    ciudad = "osorno"
)