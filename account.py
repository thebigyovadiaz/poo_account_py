class Account(object):
	def __init__(self, numeroCuenta, cantidad = 0.0):
		self._numCuenta = numeroCuenta
		self._saldo = cantidad
		
	def retirarDinero(self, cantidad):
		self._saldo -= cantidad
		
	def depositarDinero(self, cantidad):
		self._saldo += cantidad
		
	def getSaldo(self):
		return self._saldo
		
	def getNumeroCuenta(self):
		return self._numCuenta
