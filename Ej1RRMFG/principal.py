import random

def generarNumeroAleatorio(min,max):
    return random.randint(min, max)

def generarPartida():
    puntos = 0
    intentos = 0
    while True:
        numero = generarNumeroAleatorio(1,11)
        puntos = puntos + numero
        intentos = intentos + 1
        if puntos > 15:
            break
    return puntos, intentos

def final(croupierPuntos,jugadorPuntos,jugadorIntentos,croupierIntentos):
    if jugadorPuntos > croupierPuntos:
        print("(Jugador) Has Ganado!!")
    if jugadorPuntos < croupierPuntos:
        print("(Banca) ha ganado!!")
    if jugadorPuntos == croupierPuntos:
        if jugadorIntentos > croupierIntentos:
             print("(Banca) ha perdido!!")
        if jugadorIntentos < croupierIntentos:
            print("(Jugador) Has perdido!!")

def subMenu(croupierPuntos,jugadorPuntos,jugadorIntentos,croupierIntentos):
    print("\n¿Seguir Jugando?")
    print("1-Si\n2-No\n")
    opcion = int(input("Introduzca opcion: \n"))
    if opcion == 1:
        menu()
    if opcion == 2:
        final(croupierPuntos,jugadorPuntos,jugadorIntentos,croupierIntentos)

def estadoPartida(jugadorPuntos,croupierPuntos,jugadorIntentos,croupierIntentos):
    print("Puntuacion del jugador: ", jugadorPuntos)
    if jugadorPuntos > 21:
        print("(Jugador) Has perdido!!")
    if jugadorPuntos == 21:
        print("(Croupier) ha perdido!!")
    if jugadorPuntos < 21:
        subMenu(croupierPuntos,jugadorPuntos,jugadorIntentos,croupierIntentos)

def dificultad(dificil):
   jugadorPuntos,jugadorIntentos = generarPartida()
   croupierPuntos,croupierIntentos = generarPartida()
   if dificil == False:
      print("Puntuacion del croupier: ", croupierPuntos)
   estadoPartida(jugadorPuntos,croupierPuntos,jugadorIntentos,croupierIntentos)

def menu():
  print("\n---BLACKJACK---")
  while True:
   try:
     print("\n1-Modo Facil\n2-Modo Normal\n0-Salir\n")
     opcion = int(input("Introduzca opcion: \n"))
     if opcion == 1:
        dificultad(False)
     if opcion == 2:
        dificultad(True)
     if opcion == 0:
        print("--PROGRAMA FINALIZADO--")
        exit(0)
   except ValueError:
       print("Inserte uno de los numeros del menu")

if __name__ == '__main__':
    menu()
