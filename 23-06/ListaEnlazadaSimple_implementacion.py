class Nodo:
    def __init__(self,dato):
        self.dato = dato
        #Puntero al siguiente nodo
        #El ultimo por lo general apunta a None
        self.siguiente = None


#No se necesita almacenar los nodos ya que cada nodo creado apunta al siguiente en memoria
class ListaEnlazadaSimple:
    def __init__(self):
        self.primero = None
    
    def esta_vacio(self):
        if self.primero == None:
            return True
        else:
            return False
    
    def agregar_nodo_final(self,nodo):
        if self.esta_vacio() == True:
            self.primero = nodo
        else:
            #recorrer los nodos hasta encontrar uno
            #que su nodo siguiente sea none y agregar la direccion del nuevo nodo ahi
            #luego el nuevo nodo sera el ultimo
            nodo_leyendose = self.primero
            while nodo_leyendose.siguiente != None:
                nodo_leyendose = nodo_leyendose.siguiente
                #se rompera cuando llegue a un nodo que su direccion siguiente sea None
            nodo_leyendose.siguiente = nodo

    def agregar_nodo_principio(self,nodo):
        if self.esta_vacio() == True:
            self.primero = nodo
        else:
            nodo.siguiente = self.primero
            self.primero = nodo
    
    def imprimir(self):
        if self.esta_vacio() == True:
            print("La lista esta vacia")
        else:
            nodo_leyendose = self.primero
            while nodo_leyendose != None:
                print(nodo_leyendose.dato)
                nodo_leyendose = nodo_leyendose.siguiente

    def cabecera(self):
        if self.esta_vacio() == True:
            return None
        else:
            return self.primero.dato
    
    def cola(self):
        if self.esta_vacio() == True:
            return None
        else:
            nodo_leyendose = self.primero
            while nodo_leyendose.siguiente != None:
                nodo_leyendose = nodo_leyendose.siguiente
            return nodo_leyendose.dato
    
    def existe_dato(self,dato_buscar):
        nodo_leyendose = self.primero
        existe = False
        while nodo_leyendose != None:
            if nodo_leyendose.dato == dato_buscar:
                existe = True
                break
            nodo_leyendose = nodo_leyendose.siguiente
        if existe == True:
            return True
        else:
            return False
        
    def borrar(self,dato_nodo_borrar):
        if self.existe_dato(dato_nodo_borrar) == True:
            nodo_anterior = None
            nodo_leyendose = self.primero
            #mientras el dato del nodo que se esta leyendo sea distinto del dato que se desea borrar
            #
            while nodo_leyendose.dato != dato_nodo_borrar:
                #el nodo anterior pasara a ser el nodo que se esta leyendo
                nodo_anterior = nodo_leyendose
                #el nodo que se esta leyendo sera el siguiente del mismo
                nodo_leyendose = nodo_leyendose.siguiente
            #una vez que se termina el bucle, que se rompera cuando se llegue al nodo que se quiere borrar
            #nodo_anterior quedara siendo el nodo anterior al nodo que se quiere borrar
            #si sigue siendo None, significa que no se paso por el bucle
            # por lo tanto el nodo que se desea eliminar sera si o si el primer nodo
            # por lo tanto para eliminar el nodo, el primero sera el siguiente del nodo primero
            if nodo_anterior == None:
                self.primero = self.primero.siguiente
            #si es que el nodo anterior no es None
            #el nodo siguiente del anterior sera el nodo siguiente del nodo que se quiere borrar
            else:
                nodo_anterior.siguiente = nodo_leyendose.siguiente
            return True
        else:
            #Retorna falso si el nodo no se pudo borrar
            return False