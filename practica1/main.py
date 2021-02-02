#Algoritmo que pida tres números, obten la media muestralos ordenados (de mayor a menor).


def pedirNumero():
    return int (input("Introduce Numero: "))

def calculo():
    try:
        numeros = [pedirNumero(), pedirNumero(), pedirNumero()]
        mayorMenor(numeros)
        acumulador = 0
        contador = 0
        for numero in numeros:
            acumulador = acumulador + numero
            contador = contador + 1
        print("La media es: ", (acumulador / contador))

    except ZeroDivisionError:
         print("División por cero!")


def mayorMenor(numeros):
    for numero in numeros:
        if (numero < numeros[0]):
            print("Numero menor: ", numero)
        if (numero > numeros[0]):
            print("Numero mayor: ", numero)



if __name__ == '__main__':
    while True:
        try:
            calculo()
            break
        except ValueError:
            print("¡Debe introducir NUMEROS!")
