from ListaEnlazadaSimple_implementacion import ListaEnlazadaSimple, Nodo

lista_enlazada = ListaEnlazadaSimple()

while True:
    print(f"=====*=====")
    print(f"A.Agregar una fruta al final de la lista\nB.Agregar una fruta al inicio\nC.Eliminar una fruta\nD.Imprimir lista actual\nE.Obtener cabecera\nF.Obtener cola\n")
    opcion = input().lower()
    if opcion == "a":
        dato = input("\nIngrese el dato ")
        lista_enlazada.agregar_nodo_final(Nodo(dato))
    elif opcion == "b":
        dato = input("\nIngrese el dato ")
        lista_enlazada.agregar_nodo_principio(Nodo(dato))
    elif opcion == "c":
        dato = input("\nDato a eliminar ")
        accion = lista_enlazada.borrar(dato)
        if accion == True:
            print("\nEl dato ha sido borrado")
        else:
            print("\nEl dato no ha sido borrado, quiza no existe?")
    elif opcion == "d":
        lista_enlazada.imprimir()
    elif opcion == "e":
        print(lista_enlazada.cabecera())
    elif opcion == "f":
        print(lista_enlazada.cola())
    else:
        break