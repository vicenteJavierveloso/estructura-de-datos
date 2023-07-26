from ListaEnlazadaBidireccional import Nodo, ListaEnlazadaBidireccional

lista_tareas = ListaEnlazadaBidireccional()
lista_tareas.agregar_nodo_principio(Nodo(1))

while True:
    print(f"\n====*=====")
    print(f"A.Agregar Tarea al principio de la lista\nB.Agregar Tarea al final de la lista")
    print(f"C.Eliminar tarea\nD.Buscar tarea\nE.Cambiar estado tarea\nF.Mostrar tareas en orden ascendente")
    print(f"Cualquier otra letra.Salir del programa")
    opcion = input().lower()
    if opcion == "a":
        ...

    elif opcion == "b":
        ...

    elif opcion == "c":
        lista_tareas.imprimir()
    
    elif opcion == "d": 
        ...
    
    elif opcion == "e": 
        ...

    elif opcion == "f": 
        ...

    else:
        break