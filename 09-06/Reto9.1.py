class Stack:
    def __init__(self):
        self.top = None
        self.stack = []
    def push(self,item):
        self.top = item
        self.stack.append(item)
        return self.top
    def pop(self):
        if not self.is_empty():
            self.stack.pop()
            if self.is_empty():
                self.top = None
            else:
                self.top = self.stack[-1]
            return self.top
        else:
            raise IndexError("El stack esta vacio")
    def __str__(self):
        return str(self.stack)
    def is_empty(self):
        return len(self.stack) == 0
    def size(self):
        return len(self.stack)

libros = Stack()
while True:
    print(libros)
    try:
        opcion = int(input(f"0 para desapilar libro, 1 para apilar libro "))
        if opcion == 0:
            if libros.is_empty():
              exit()
            else:
                libros.pop()
        elif opcion == 1:
            libros.push(input(f"Nombre del libro "))
    except ValueError:
        print(f"Opcion invalida")
