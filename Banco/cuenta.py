from typing import Any, Union


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

      def __init__(self,titular):
         super().__init__(titular)
         self.__saldoPrenium = 0

      def setInteres(self,interes):
         self.__interes = interes

      def ingresarPrenium(self,importe):
          self.__saldoPrenium = self.__saldoPrenium + importe

      def retirarPrenium(self,cantidad):
          self.__saldoPrenium = self.__saldoPrenium - cantidad

      def getSaldoPrenium(self):
          return self.__saldoPrenium

      def getPlusvalia(self):
          self.__saldoPrenium = self.__saldoPrenium + (self.__saldoPrenium * (self.__interes / 100))
          return self.__saldoPrenium
