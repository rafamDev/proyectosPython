#Algoritmo que pida tres números, obtenga la media de ellos y los muestre ordenados (de mayor a menor).


def pedirNumero():
    return float (input("Introduce Numero: "))

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
    mayor = numeros[0]
    menor = numeros[0]
    for numero in numeros:
        if numero > mayor:
            mayor = numero
        if numero < menor:
            menor = numero
    print("Numero mayor: ", mayor)
    print("Numero menor: ", menor)


if __name__ == '__main__':
    while True:
        try:
            calculo()
            break
        except ValueError:
            print("¡Debe introducir NUMEROS!")
