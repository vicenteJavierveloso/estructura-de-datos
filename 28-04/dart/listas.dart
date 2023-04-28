void main() {
  print("Listas numericas");
  List<int> enteros = [1,2,3,4,5,6,7,8,9];
  for (int i=1; i <= 1; i++) {
    enteros.add(i);
  }

  print("impresion vertical de la lista");
  for (int i =0; i<enteros.length; i++){
    print(enteros[i]);
  }

  List<int> listagenerada = List.generate(10, (i) => i+1);
  print("Lista generada $listagenerada");
  
  print("lista de strings");
  List<String> nombres =["tito","pepe"];
  print("lista de strings $nombres");

  List<String> colores = List<String>.from(["Azul", "Rojo", "Verde"]);
  print("Lista colores $colores");

  print("Consultar elementos");
  print(nombres.last);
  print(nombres[0]);
  print(nombres.elementAt(1));
}