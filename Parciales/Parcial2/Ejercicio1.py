from ListaCircularSimple import ListaCircularSimple, Nodo

lista_reproduccion = ListaCircularSimple()
lista_reproduccion.agregar_nodo_principio(Nodo("Video de prueba","Yo", "1:00"))

while True:
    print(f"\n====*=====")
    print(f"A.Agregar videos al principio de la lista\nB.Agregar videos al final de la lista\nC.Mostrar lista de reproduccion\nD.Buscar video\nE.Eliminar video\nF.Verificar si esta vacia")
    print(f"Cualquier otra letra.Salir del programa")
    opcion = input().lower()
    if opcion == "a":
        titulo = input("Titulo del video ")
        autor = input("Autor del video ")
        duracion = input("Duracion del video ")
        lista_reproduccion.agregar_nodo_principio(Nodo(titulo,autor,duracion))

    elif opcion == "b":
        titulo = input("Titulo del video ")
        autor = input("Autor del video ")
        duracion = input("Duracion del video ")
        lista_reproduccion.agregar_nodo_final(Nodo(titulo,autor,duracion))

    elif opcion == "c":
        lista_reproduccion.imprimir()
    
    elif opcion == "d": #Buscar video
        titulo = input("Titulo del video ")
        autor = input("Autor del video ")
        duracion = input("Duracion del video ")
        accion = lista_reproduccion.buscar_nodo(titulo,autor,duracion)
        if accion == True:
            print("El video existe en la lista de reproduccion")
        else:
            print("El video no existe en la lista de reproduccion")
    
    elif opcion == "e": #Eliminar video
        titulo = input("Titulo del video ")
        autor = input("Autor del video ")
        duracion = input("Duracion del video ")
        accion = lista_reproduccion.eliminar_nodo(titulo,autor,duracion)
        if accion == True:
            print("El video fue eliminado de la lista de reproduccion")
        else:
            print("El video no pudo ser eliminado de la lista de reproduccion")

    elif opcion == "f": #Verificar si esta vacia
        accion = lista_reproduccion.esta_vacia()
        if accion == True:
            print("La lista esta vacia")
        else:
            print("La lista no esta vacia")

    else:
        break