main() {
  var op1 = operacion(20, 10, suma);
  var op2 = operacion(20, 10, resta);
  print(op1);
  print(op2);
}
//Las funciones se definen despues de la funcion principal main
//El parametro func es del tipo funcion
int operacion(int a, int b, Function func) {
  return func(a, b);
}

//Las funciones se pueden usar como parametros
int suma(int a, int b) {
  return a + b;
}

int resta(int a, int b) {
  return a - b;
}
