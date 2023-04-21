main(){
    //Declarando valores de tipo entero
    int a = 1;
    int b = 2;
    int c = 3;
    //Operadores comunes
    print("01-Operadores aritmeticoas");
    print("Suma entre a y b es ${a+b}");

    //Variables de tipo reales
    double e = 20.55;
    double f = 5.90;
    double g = 9.81234;
    //Entrega valores reales con todos sus decimales
    print("El valor de g con todos sus decimales: $g");

    //Entrega el valor con pocos decimales o decimales especificos
    double num1 = double.parse((g).toStringAsFixed(2));
    print("El valor de g con solamente dos decimales: $num1");
}