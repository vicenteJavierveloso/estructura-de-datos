class NodoArbol:
    def __init__(self,nombre):
        self.nombre = nombre
        self.hijos = []

    def agregar_hijo(self,hijo):
        self.hijos.append(hijo)

    def mostrar_arbol(self, nivel = 0):
        identacion = "  " *nivel
        print(identacion +self.nombre)
        for hijo in self.hijos:
            hijo.mostrar_arbol(nivel + 1)
            