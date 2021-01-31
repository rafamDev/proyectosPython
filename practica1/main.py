#Algoritmo que pida tres números y los muestre ordenados (de mayor a menor).

def pedirNumero():
    return int (input("Introduce Numero: "))

def ordenarNumeros():
    numeros = [pedirNumero(),pedirNumero(),pedirNumero()]
    numeros.sort()
    print("Numeros ordenados de menor a meyor: ",numeros)
    numeros.sort(reverse=True)
    print("Numeros ordenados de mayor a menor: ",numeros)


if __name__ == '__main__':
    ordenarNumeros()