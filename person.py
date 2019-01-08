from account import Account

class Person(object):
	def __init__(self, nombre, apellido):
		self.__nombre = nombre
		self.__apellido = apellido
		
	def setNombre(self, nombre):
		self.__nombre = nombre
		
	def getNombre(self):
		return self.__nombre
		
	def setApellido(self, apellido):
		self.__apellido = apellido
		
	def getApellido(self):
		return self.__apellido
