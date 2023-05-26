//Vicente Javier Veloso Gomez
import 'dart:io';
import 'dart:math';
void main() {
  List <int> lista1 = [];
  List <int> lista2 = [];
  List <int> lista3 = [];
  //Lista 1 y 2 con elementos aleatorios del 10 al 20
  for (int i = 0; i<10; i++) {
    lista1.add(Random().nextInt(11) + 10);
    lista2.add(Random().nextInt(11) + 10);
  }
  //Lista 3 se llena por teclado
  for (int i = 0; i<5; i++) {
    print("Ingresar elemento $i");
    lista3.add(int.parse(stdin.readLineSync()!));
  }
  //Mostrar listas
  print("Lista 1: $lista1\nLista 2: $lista2\nLista 3: $lista3");
  //Concatenar
  List <int> lista4 = lista1+lista2+lista3;
  print("Lista 1, 2 y 3 concatenadas: $lista4");
  //Sumar todos los elementos
  int suma = 0;
  for (int i = 0; i<lista4.length; i++) {
    suma += lista4[i];
  }
  //promedio
  double promedio = suma/lista4.length;
  print("Promedio de los elementos de las listas concatenadas: $promedio");
  //ordenar ascendentemente
  lista4.sort();
  print("Lista concatenada ordenada ascendentemente: $lista4");
}