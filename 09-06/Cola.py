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
    
fila = Cola()

for i in range(5):
    fila.encolar(i+1)
print(fila)
fila.desencolar()
print(fila)