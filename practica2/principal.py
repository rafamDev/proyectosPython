
from cuenta import Cuenta

def ingresar(cuenta,ingreso):
    cuenta.ingresar(ingreso)
    mostrarDatos(cuenta.getTitular(), cuenta.getSaldo())
    print(cuenta.getTitular(), "ha ingresado ", ingreso, "€")
    print("---- FIN DE LA OPERACION ----")

def retirar(cuenta,retirada):
    cuenta.retirar(retirada)
    mostrarDatos(cuenta.getTitular(),cuenta.getSaldo())
    print(cuenta.getTitular(), "ha retirado ", retirada, "€")
    print("---- FIN DE LA OPERACION ----")


def mostrarDatos(titular,saldo):
    print("Titular: ", titular)
    print("Saldo total: ", saldo , "€")


def subMenu(cuenta):
    while True:
       opcion2 = int(input("1-Ingresar 2-Retirar 3-Volver "))
       if opcion2 == 3:
           break
           cantidad = float(input("Inserte Cantidad: "))
       if opcion2 == 1:
           ingresar(cuenta, cantidad)
       elif opcion2 == 2:
           retirar(cuenta, cantidad)
       else:
           print("Debe ingresar uno de los numeros solicitados.")

def menu():
    while True:
       opcion1 = int(input("1-Inicio 2-Salir "))
       if opcion1 == 1:
           nombre = input("Inserte Titular de cuenta: ")
           cuenta = Cuenta(nombre)
           subMenu(cuenta)
       if opcion1 == 2:
           exit(0)

if __name__ == '__main__':
     menu()