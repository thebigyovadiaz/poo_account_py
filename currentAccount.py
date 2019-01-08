from account import Account
from person import Person

class CurrentAccount(Account):
	def __init__(self, nombre, apellido, numeroCuenta, cantidad, tipo = 0.0, tarjetaDebito = False, tarjetaCredito = False, cuota = 0.0):
		Account.__init__(self, numeroCuenta, cantidad)
		self.__tipoInteres = 1 + float(tipo)
		self.__tarjetaDebito = tarjetaDebito
		self.__tarjetaCredito = tarjetaCredito
		self.__cuotaMantenimiento = cuota
		self.__persona = Person(nombre, apellido)
		
	def getTipoInteres(self):
		return self.__tipoInteres
		
	def setTipoInteres(self, interes):
		self.__tipoInteres = interes
		
	def getTarjetaDebito(self):
		return self.__tarjetaDebito
		
	def setTarjetaDebito(self, tajeta):
		self.__tarjetaDebito = tarjeta
		
	def getTarjetaCredito(self):
		return self.__tarjetaCredito
		
	def setTarjetaCredito(self, tajeta):
		self.__tarjetaCredito = tarjeta
		
	def getCuotaMantenimiento(self):
		return self.__cuotaMantenimiento
		
	def setCuotaMantenimiento(self, cuota):
		self.__cuotaMantenimiento = cuota
		
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
