class Nodo:
    def __init__(self,ID,titulo,descripcion,estado = "Pendiente"):
        self.ID = ID
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado

        #caracteristicas del nodo
        #apunta al nodo anterior
        self.anterior = None
        #apunta al nodo siguiente
        self.siguiente = None
    

class ListaEnlazadaBidireccional:
    def __init__(self):
        self.primero = None
    
    def esta_vacia(self):
        if self.primero == None:
            return True
        else:
            return False
    
    def agregar_nodo_principio(self, nodo:Nodo):
        if self.esta_vacia() == True:
            self.primero = nodo
            return True
        else:
            self.primero.anterior = nodo
            nodo.siguiente = self.primero
            self.primero = nodo
            return True
        
    def agregar_nodo_final(self, nodo:Nodo):
        if self.esta_vacia() == True:
            self.primero = nodo
            return True
        else:
            #necesito llegar al final
            nodo_temporal = self.primero
            while nodo_temporal != None:
                nodo_temporal = nodo_temporal.siguiente
            #termina cuando llega al ultimo
            nodo_temporal.siguiente = nodo
            nodo.anterior = nodo_temporal
            return True
    
    def imprimir(self):
        if self.esta_vacia() == False:
            nodo_leyendose = self.primero
            while nodo_leyendose != None:
                print(f"Titulo: {nodo_leyendose.titulo}, Descripcion: {nodo_leyendose.descripcion}, Estado: {nodo_leyendose.estado}")
                nodo_leyendose = nodo_leyendose.siguiente
        else:
            print(f"La lista esta vacia")

    def buscar_nodo(self,ID,titulo,descripcion,estado):
        existe = False
        nodo_leyendose = self.primero
        while nodo_leyendose != None:
            if nodo_leyendose.ID == ID and nodo_leyendose.titulo == titulo and nodo_leyendose.descripcion == descripcion and nodo_leyendose.estado == estado:
                existe = True
                break
        if existe == True:
            return True
        else:
            return False
    def imprimir_ascendente(self):
        lista = []
        nodo_leyendose = self.primero
        while nodo_leyendose != None:
            ...
    
    def cambiar_estado(self,ID,titulo,descripcion,estado,nuevo_estado):
        if self.buscar_nodo(ID,titulo,descripcion,estado) == True:
            nodo_a_cambiar = self.primero
            while nodo_a_cambiar != None:
                if nodo_a_cambiar.ID == ID and nodo_a_cambiar.titulo == titulo and nodo_a_cambiar.descripcion == descripcion and nodo_a_cambiar.estado == estado:
                    nodo_a_cambiar.estado = nuevo_estado
                    break
            return True
        else:
            #retorna falso porque el nodo no existe
            return False
    def eliminar_nodo(self,titulo,autor,duracion):
        ...
