palabra = input("Ingresar palabra ")
palabra = list(palabra)
vocales = ["a","e","i","o","u"]
for i in range(len(vocales)):
    print(f"{vocales[i]} = {palabra.count(vocales[i])}")