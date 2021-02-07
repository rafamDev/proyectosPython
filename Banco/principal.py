
# El siguiente programa simula ser un cajero que acepta dos tipos de tarjetas, una normal (débito), donde se ingresa y retira capital
# y otra prenium (crédto) donde introduciendo un porcentaje de incremento se crea un intrés compuesto a cada ingreso.

from cuenta import Cuenta, CuentaPrenium

def ingresar(cuenta,ingreso):
    cuenta.ingresar(ingreso)
    print("Titular: ", cuenta.getTitular())
    print("Saldo total: ", cuenta.getSaldo(), "€")
    print(cuenta.getTitular(), "ha ingresado ", ingreso, "€")
    print("---- FIN DE LA OPERACION ----")

def retirar(cuenta,cantidad):
    print("Titular: ", cuenta.getTitular())
    if cuenta.getSaldo() < cantidad:
        print("****NO HAY SALDO SUFICIENTE****")
    else:
        cuenta.retirar(cantidad)
        print(cuenta.getTitular(), "ha retirado: ", cantidad, "€")
    print("Saldo total: ", cuenta.getSaldo(), "€")
    print("---- FIN DE LA OPERACION ----")

def ingresarPrenium(cuentaPrenium, ingreso):
    cuentaPrenium.ingresarPrenium(ingreso)
    print("Titular: ", cuentaPrenium.getTitular())
    print("Saldo total cuenta PRENIUM: ", "%.2f" % cuentaPrenium.getPlusvalia(), "€")
    print(cuentaPrenium.getTitular(), "ha ingresado ", ingreso, "€")
    print("---- FIN DE LA OPERACION ----")

def retirarPrenium(cuentaPrenium, cantidad):
    print("Titular: ", cuentaPrenium.getTitular())
    if cuentaPrenium.getSaldoPrenium() < cantidad:
        print("****NO HAY SALDO SUFICIENTE****")
    else:
        cuentaPrenium.retirarPrenium(cantidad)
        print(cuentaPrenium.getTitular(), "ha retirado: ", cantidad, "€")

    print("Saldo total: ", "%.2f" % cuentaPrenium.getSaldoPrenium(), "€")
    print("---- FIN DE LA OPERACION ----")

def subMenu(cuenta):
    while True:
     try:
       opcion = int(input("\n1-Ingresar 2-Retirar 3-Volver\n "))
       if opcion == 3:
           break
       if opcion == 1:
           cantidad = float(input("Inserte Cantidad: "))
           ingresar(cuenta, cantidad)
       if opcion == 2:
           cantidad = float(input("Inserte Cantidad: "))
           retirar(cuenta, cantidad)
       else:
           print("Debe ingresar uno de los numeros solicitados.")
     except ValueError:
        print("Ingrese uno de los numeros solicitados.")

def subMenuPrenium(cuentaPrenium):
    cuentaPrenium.setInteres(float(input("Inserte interes en (%): ")))
    while True:
     try:
       opcion = int(input("\n1-Ingresar 2-Retirar 3-Volver\n "))
       if opcion == 3:
           break
       if opcion == 1:
           cantidad = float(input("Inserte Cantidad: "))
           ingresarPrenium(cuentaPrenium,cantidad)
       if opcion == 2:
           cantidad = float(input("Inserte Cantidad: "))
           retirarPrenium(cuentaPrenium,cantidad)
       else:
           print("Debe ingresar uno de los numeros solicitados.")
     except ValueError:
        print("Ingrese uno de los numeros solicitados.")

def menu():
    while True:
     try:
       opcion1 = int(input("1-Inicio 2-Salir "))
       if opcion1 == 1:
           opcionCuenta = int(input("1-Cuenta 2-Cuenta Prenium"))
           nombre = input("Inserte Titular de cuenta: ")
           if opcionCuenta == 1:
               cuenta = Cuenta(nombre)
               subMenu(cuenta)
           if opcionCuenta == 2:
               cuentaPrenium = CuentaPrenium(nombre)
               subMenuPrenium(cuentaPrenium)
       if opcion1 == 2:
           print("--PROGRAMA CERRADO--")
           exit(0)
     except ValueError:
        print("Ingrese uno de los numeros solicitados.")


if __name__ == '__main__':
     menu()