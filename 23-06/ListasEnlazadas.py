class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazadas:
    def __init__(self):
        self.primero = None
        self.ultimo = None
    
    def esta_vacia(self):
        return self.primero is None
    
    def agregar_final(self,dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.primero = nuevo_nodo
            
    