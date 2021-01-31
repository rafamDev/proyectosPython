
def entrada():
    nombreProducto = input("Introduce nombre producto: ")
    cantidad = int (input("Introduce cantidad: "))
    precio = float (input("Introduce precio: "))
    salida(nombreProducto,cantidad,precio)

def salida(nombreProducto,cantidad,precio):
    print("El nombre del producto es:",nombreProducto)
    print("Cantidad:",cantidad,", ",end="") #end="" evita un salto de linea. #print("Cantidad: ",str(cantidad))
    print("Precio: %.2f"%(precio))

def funcion():
    entrada()

if __name__ == '__main__':
   funcion()