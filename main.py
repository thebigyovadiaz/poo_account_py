from person import Person
from currentAccount import CurrentAccount
from savingAccount import SavingAccount
import time
import pickle
import sys
import os

numCuentas = 0
clientes = []
opcion = 0

def abrirCuenta(numCuentas):
	try:
		opcion = int(input('''Seleccione el tipo de cuenta a aperturar: 
		1. Cuenta de Ahorro
		2. Cuenta Corriente
		'''))
		
		if opcion == 1:			
			nombre = input('Ingrese Nombre: ')
			apellido = input('Ingrese Apellidos: ')
			cantidad = input('Monto inicial de apertura: ')
			tipoInteres = input('Tipo de interes: ')
			tarjetaD = input('Tarjeta de Débito (1-Sí,0-No): ')			
			if (tarjetaD == '1'):
				tarjetaDebito = True
			else:
				tarjetaDebito = False
				
			tarjetaC = input('Tarjeta de Crédito (1-Sí,0-No): ')			
			if (tarjetaC == '1'):
				tarjetaCredito = True
			else:
				tarjetaCredito = False
				
			cuotaMantenimiento = input('Cuota de mantenimiento: ')
			personaAux = CurrentAccount(nombre, apellido, numCuentas, float(cantidad), float(tipoInteres), tarjetaDebito, tarjetaCredito, float(cuotaMantenimiento))
			
			return personaAux
			
		elif opcion == 2:
			nombre = input('Ingrese Nombre: ')
			apellido = input('Ingrese Apellidos: ')
			cantidad = input('Monto inicial de apertura: ')
			tipoInteres = input('Tipo de interes: ')
			fecha = time.strftime("%d/%m/%y")
			personaAux = SavingAccount(nombre, apellido, numCuentas, float(cantidad), fecha, float(tipoInteres))
			return personaAux
			
		else:
			return
		
		print('Se creó la cuenta con éxito.')
		input('Pulse Enter para continuar...')	
	except ValueError:
		print('Se debe introducir sólo números')
		
try:
	with open('cuentas.txt', 'rb') as f:
		clientes = pickle.load(f)
except:
	f = open('cuentas.txt', 'wb')
	f.close()

while (opcion != 6):
	try:
		opcion = int(input('''Seleccione la operación a realizar:
		1. Abrir una cuenta
		2. Ver cuentas
		3. Ver saldo
		4. Hacer Depósito
		5. Hacer Retiro
		6. Salir
		'''))
	
		if opcion == 1:
			clienteAux = abrirCuenta(numCuentas)
			if clienteAux is not None:
				clientes.append(clienteAux)
				numCuentas += 1
				
		elif opcion == 2:
			for cliente in clientes:
				print('Nombre: ' + cliente.getNombre())
				print('Apellido: ' + cliente.getApellido())
				print('Numero de Cuenta: ' + str(cliente.getNumeroCuenta()))
				print('\n')
			input("Pulse Enter para continuar...")
			
		elif opcion == 3:
			cuenta = int(input('Ingrese la cuenta a consultar: '))
			print('El saldo de la cuenta ' + str(cuenta) + ' es de: ' + str(clientes[cuenta].getSaldo()) + ' Dólares.')
			input('Pulse Enter para continuar...')
			os.system('cls')
		elif opcion == 4:
			cuenta = int(input('Ingrese la cuenta a depositar el dinero: '))
			cantidad = int(input('Ingre la cantidad de dinero a depositar: '))
			clientes[cuenta].depositarDinero(cantidad)
			print('Se realizó el depósito con éxito.')
			input('Pulse Enter para continuar...')
			os.system('cls')
		elif opcion == 5:
			cuenta = int(input('Ingrese la cuenta a retirar el dinero: '))
			cantidad = int(input('Ingre la cantidad de dinero a retirar: '))
			clientes[cuenta].retirarDinero(cantidad)
			print('Se realizó el retiro con éxito.')
			input('Pulse Enter para continuar...')
			os.system('cls')
	except ValueError:
		print('Se debe introducir sólo números')

with open('cuentas.txt', 'wb') as f:
	pickle.dump(clientes, f)
		
print('Fin del programa')
