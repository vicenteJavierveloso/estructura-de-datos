//Ejercicio 5
import 'dart:io';
void main() {
  //Solicita cantidad de elementos
  print("Ingresar cantidad de elementos ");
  //Recibe un string pero lo parsea a un entero para trabajarlo como tal
  int n = int.parse(stdin.readLineSync()!);
  //Define una lista que contendra solo enteros
  List<int> lista_de_elementos = [];
  //Ciclo for que ira desde 0 hasta la cantidad de elementos que pidio el usuario
  for (int i=0; i<n; i++){
    //Solicita ingrese un elemento
    print("Ingresar elemento ");
    //Se establece que elemento es un entero y se le va dando valores segun lo que ingrese el usuario
    int elemento = int.parse(stdin.readLineSync()!);
    //añade a la lista
    lista_de_elementos.add(elemento);
  }
  //Crea una variable que contendra la suma, de tipo entero
  int suma = 0;
  //Ciclo for desde 0 hasta la cantidad total de elementos que tenga la lista
  for (int i=0; i<lista_de_elementos.length; i++) {
    //Suma uno por uno los elementos
    suma = suma + lista_de_elementos[i];
  }
  //Imprime la suma
  print("La suma de los elementos ingresados es $suma");
}