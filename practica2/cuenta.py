
class Cuenta():

    def __init__(self,titular):
        self.__titular = titular
        self.__saldo = 0

    def ingresar(self,importe):
        self.__saldo = self.__saldo + importe

    def retirar(self,importe):
        self.__saldo = self.__saldo - importe

    def getTitular(self):
        return self.__titular

    def getSaldo(self):
        return self.__saldo


class CuentaPrenium(Cuenta):
      print()