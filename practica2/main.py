#Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.

def pedirDatos():
    mostrarDatos(input("Introduce Nombre: "),
                 input("Introduce Primer Apellido: "),
                 input("Introduce Segundo Apellido: "))


def mostrarDatos(nombre,apellido1,apellido2):
    print(nombre[0],apellido1[0],apellido2[0],sep=",",end="")


def funcion():
    pedirDatos()


if __name__ == '__main__':
    funcion()
