class Cola:
    def __init__(self):
        self.items = []
    def encolar(self, elemento):
        self.items.append(elemento)
    def desencolar(self):
        if self.isEmpty():
            raise ValueError("La cola esta vacia")
        return self.items.pop(0)
    def isEmpty(self):
        return len(self.items) == 0
    def __str__(self):
        return str(self.items)
    def size(self):
        return len(self.items)

cola_de_banco = Cola()

while True:
    print(f"Cola actual: {cola_de_banco}")
    try:
        opcion = int(input(f"0 para encolar persona, 1 para desencolar persona "))
        if opcion == 0:
            if cola_de_banco.isEmpty():
                exit()
            else:
                cola_de_banco.desencolar()
        elif opcion == 1:
            cola_de_banco.encolar(input(f"Nombre persona: "))
    except ValueError:
        print(f"Opcion invalida")
