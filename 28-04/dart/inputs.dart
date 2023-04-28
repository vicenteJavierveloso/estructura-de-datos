import 'dart:io';
void main() {
  print("Ingrese su nombre");
  String nombre = stdin.readLineSync()!;
  print("Hola, $nombre");
  print("Solicitando un numero");
  int edad = int.parse(stdin.readLineSync()!);
  print("Edad $edad");
}