from figuras import Triangulo, Rectangulo, Cuadrado, Pentagono

def rectangulo():
    rectangulo = Rectangulo(float(input("Introduzca Base: ")),float(input("Introduzca Altura: ")))
    print("El area es: ",rectangulo.calcularArea())
    print("El perimetro es: ",rectangulo.calcularPerimetro())

def triangulo():
    triangulo = Triangulo(float(input("Introduzca Lado(1) [Base]: ")),float(input("Introduzca [Altura]: ")),float(input("Introduzca Lado(2): ")),float(input("Introduzca Lado(3): ")))
    print("El area es: ",triangulo.calcularArea())
    print("El perimetro es: ",triangulo.calcularPerimetro())

def cuadrado():
    cuadrado = Cuadrado(float(input("Introduzca Lado: ")))
    print("El area es: ", cuadrado.calcularArea())
    print("El perimetro es: ", cuadrado.calcularPerimetro())

def pentagono():
   pentagono = Pentagono(float(input("Introduzca Lado: ")),float(input("Introduzca Apotema: ")))
   print("El area es: ", pentagono.calcularArea())
   print("El perimetro es: ", pentagono.calcularPerimetro())

def subMenu(opcion):
    if opcion == 0:
        print("--PROGRAMA FNALIZADO--")
        exit(0)
    if opcion == 1:
        triangulo()
    if opcion == 2:
        rectangulo()
    if opcion == 3:
        cuadrado()
    if opcion == 4:
        pentagono()

def menu():
  print("\n**FIGURAS GEOMETRICAS**")
  while True:
   try:
    print("\n1-Triangulo 2-Rectangulo 3-Cuadrado 4-Pentagono 0-Salir")
    subMenu(int(input("Escoja una opcion: \n")))
   except ValueError:
    print("Seleccione uno de los parametros solicitados")

if __name__ == '__main__':
    menu()