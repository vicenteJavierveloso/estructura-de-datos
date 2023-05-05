//Ejercicio 6
import 'dart:math';
void main(){
  List<int> arreglo = [];
  //Valor de elementos del arreglo entre 10 y 30
  int n = Random().nextInt(20)+10;
  //Ciclo for que llena el arreglo con elementos de 1 a 10 hasta que se complete el numero
  //de elementos que se definio antes
  for (int i = 0; i<n; i++){
    arreglo.add(Random().nextInt(10));
  }
  //Imprime el arreglo sin ordenar
  print("Arreglo sin ordenar $arreglo");
  //Ordena el arreglo usando un metodo propio de las listas y lo imprime una ves ordenado
  arreglo.sort();
  print("Arreglo ordenado $arreglo");
  //Ordena aleatoriamente el arreglo
  arreglo.shuffle();
  print("Arreglo desordenado $arreglo");
}

