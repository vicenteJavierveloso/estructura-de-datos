class Nodo:
    def __init__(self,titulo,autor,duracion):
        self.titulo = titulo
        self.autor = autor
        self.duracion = duracion

        #caracteristicas del nodo
        #apunta al nodo anterior
        self.anterior = None
        #apunta al nodo siguiente
        self.siguiente = None
    

class ListaCircularSimple:
    def __init__(self):
        self.primero = None
    
    def esta_vacia(self):
        if self.primero == None:
            return True
        else:
            return False
    
    def agregar_nodo_principio(self, nodo:Nodo):
        if self.esta_vacia() == True:
            nodo.siguiente = nodo
            nodo.anterior = nodo
            self.primero = nodo
            return True
        else:
            temp_ultimo = self.primero
            while temp_ultimo.siguiente != self.primero:
                temp_ultimo = temp_ultimo.siguiente
            #cuando se rompa el bucle se habra llegado al nodo ultimo
            #actualizar el siguiente de dicho nodo por el nuevo nodo
            temp_ultimo.siguiente = nodo
            nodo.siguiente = self.primero
            self.primero = nodo
            return True
        
    def agregar_nodo_final(self, nodo:Nodo):
        if self.esta_vacia() == True:
            nodo.siguiente = nodo
            nodo.anterior = nodo
            self.primero = nodo
            return True
        else:
            #necesito llegar al final
            temp_ultimo = self.primero
            while temp_ultimo.siguiente != self.primero:
                temp_ultimo = temp_ultimo.siguiente
            #llegue al final y el ultimo nodo es temp_ultimo
            temp_ultimo.siguiente = nodo
            nodo.siguiente = self.primero
            return True
    
    def imprimir(self):
        if self.esta_vacia() == False:
            nodo_leyendose = self.primero
            while nodo_leyendose.siguiente != self.primero:
                print(f"{nodo_leyendose.titulo}, {nodo_leyendose.autor}, {nodo_leyendose.duracion}")
                nodo_leyendose = nodo_leyendose.siguiente
            print(f"Titulo: {nodo_leyendose.titulo}, Autor: {nodo_leyendose.autor}, Duracion: {nodo_leyendose.duracion}, Siguiente: {nodo_leyendose.siguiente.titulo}")
        else:
            print(f"La lista esta vacia")

    def buscar_nodo(self,titulo,autor,duracion):
        existe = False
        nodo_leyendose = self.primero
        while nodo_leyendose.siguiente != self.primero:
            if nodo_leyendose.titulo == titulo and nodo_leyendose.autor == autor and nodo_leyendose.duracion == duracion:
                existe = True
                break
        if nodo_leyendose.titulo == titulo and nodo_leyendose.autor == autor and nodo_leyendose.duracion == duracion:
            existe = True
        
        if existe == True:
            return True
        else:
            return False
    
    def eliminar_nodo(self,titulo,autor,duracion):
        if self.buscar_nodo(titulo,autor,duracion) == True:
            #si es que existe
            #retorna True si se realiza la eliminacion
            nodo_a_borrar = self.primero
            while nodo_a_borrar.titulo != titulo and nodo_a_borrar.autor != autor and nodo_a_borrar.duracion != duracion:
                nodo_a_borrar = nodo_a_borrar.siguiente
            #cuando se sale del bucle ya se llego al nodo a borrar
            if nodo_a_borrar.siguiente == nodo_a_borrar:
                #es el unico
                ...
            else:
                ...
        else:
            #si es que no existe
            return False
