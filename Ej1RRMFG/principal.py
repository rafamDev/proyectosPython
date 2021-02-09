import random

def generarNumeroAleatorio(min,max):
    return random.randint(min, max)

def puntuacionBanca():
    acumulador = 0
    contador = 0
    while True:
        numero = generarNumeroAleatorio(1,11)
        acumulador = acumulador + numero
        contador = contador + 1
        if acumulador > 15:
            break
    return acumulador


def subMenu():
    print("\n¿Seguir Jugando?")
    print("1-Si\n2-No\n")
    opcion = int(input("Introduzca opcion: "))
    if opcion == 1:
        dificultad("normal")


def jugador(puntuacion):
    return puntuacion


def banca(puntuacion):
    return puntuacion


def dificultad(nivel):
   puntuacion = puntuacionBanca()
   if nivel == "facil":
       print("Puntuacion del jugador: ", puntuacion)
   print("Numero aleatorio: ", generarNumeroAleatorio(1, 11))
   if puntuacion > 21:
       print("(Jugador) Has perdido!!")
       jugador(puntuacion)
   if puntuacion == 21:
       print("(Banca) ha perdido!!")
       banca(puntuacion)
   if puntuacion < 21:
       subMenu()




def normal():
    pass


def menu():
  print("\n---BLACKJACK---")
  while True:
   try:
     print("\n1-Modo Facil\n2-Modo Normal\n0-Salir\n")
     opcion = int(input("Introduzca opcion: "))
     if opcion == 1:
        dificultad("facil")
     if opcion == 2:
        normal()    
     if opcion == 0:
        print("--PROGRAMA FINALIZADO--")
        exit(0)
   except ValueError:
       print("Inserte uno de los numeros del menu")



if __name__ == '__main__':
    menu()
