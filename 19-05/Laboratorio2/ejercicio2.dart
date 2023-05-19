//Vicente Javier Veloso Gomez
import "dart:io";
import "dart:math";

void main() {
  List lista1 = [14,2,5,3,9];
  List lista2 = [];
  List lista3 = [];
  for (int i = 0; i<5; i++) {
    print("Ingrese elemento indice $i para la lista 2");
    int num = int.parse(stdin.readLineSync()!);
    lista2.add(num);
  }
  for (int i = 0; i<5; i++) {
    lista3.add(-1*(Random().nextInt(11)+15));
  }
  print("Lista 1 = $lista1");
  print("Lista 2 = $lista2");
  print("Lista 3 = $lista3");
  for (int i = 0 ; i<lista1.length; i++) {
    int aux = lista1[i]-lista2[i];
    lista1.removeAt(i);
    lista1.insert(i, aux);
  }
  print("Resta lista 1 y 2 = $lista1");
  //la lista obtenida se suma con la tercera lista
  for (int i = 0; i<lista1.length; i++) {
    int aux = lista1[i]+lista3[i];
    lista1.removeAt(i);
    lista1.insert(i, aux);
  }
  print("Suma lista obtenida con lista 3 = $lista1");
  //Insertar en la primera y segunda posicion 17 y 24
  lista1.insert(0,24);
  lista1.insert(0,17);
  print("Se añade en la primera y segunda posicion 17 y 24 a la lista obtenida = $lista1");
}