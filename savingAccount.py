from account import Account
from person import Person

class SavingAccount(Account):
	def __init__(self, nombre, apellido, numeroCuenta, cantidad, fecha, tipo = 0.0):
		Account.__init__(self, numeroCuenta, cantidad)
		self._tipoInteres = 1 + tipo
		self.__fechaApertura = fecha
		self.__persona = Person(nombre, apellido)
		
	def getTipoInteres(self):
		return self.__tipoInteres
		
	def setTipoInteres(self, interes):
		self.__tipoInteres = interes
		
	def getFecha(self):
		return self.__fechaApertura
		
	def getSaldo(self):
		return self._saldo*self.__tipoInteres
		
	def getNombre(self):
		return self.__persona.getNombre()
		
	def setNombre(self, nombre):
		self.__persona.setNombre(nombre)
		
	def getApellido(self):
		return self.__persona.getApellido()
		
	def setApellido(self, apellido):
		self.__persona.setApellido(apellido)
