from abc import ABC

class FiguraGeometrica(ABC):

    def calcularArea(self):
        pass

    def calcularPerimetro(self):
        pass

class Rectangulo(FiguraGeometrica):

    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return self.base * self.altura

    def calcularPerimetro(self):
        return 2*(self.base + self.altura)

class Triangulo(FiguraGeometrica):

    def __init__(self,base,altura,ladoA,ladoB):
       self.base = base
       self.altura = altura
       self.ladoA = ladoA
       self.ladoB = ladoB

    def calcularArea(self):
      return (self.base * self.altura)/2

    def calcularPerimetro(self):
      return self.base + self.ladoA + self.ladoB

class Pentagono(FiguraGeometrica):

    def __init__(self,lado,apotema):
        self.lado = lado
        self.apotema = apotema

    def calcularArea(self):
        return (self.calcularPerimetro() * self.apotema)/2

    def calcularPerimetro(self):
        return self.lado * 5

class Cuadrado(Rectangulo):

    def __init__(self,lado):
        super().__init__(lado,lado)

