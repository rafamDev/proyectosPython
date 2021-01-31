
def logIn(nombre,password):
    if nombre.upper() or nombre.lower() == "Pepe" and password == "1234":
        print("Usuario correcto!")
    else:
        print("Usuario Incorrecto!")


if __name__ == '__main__':
    logIn(input("Introduce nombre de ususario: "),input("Introduce password: "))
