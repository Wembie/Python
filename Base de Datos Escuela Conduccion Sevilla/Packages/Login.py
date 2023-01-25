import time
import getpass
import os

def login():
	secretarias = {
		"Usuario": [ "123", "Admin" ]
	}
	intentos = 3
	os.system( 'TITLE ESCUELA CONDUCCION SEVILLA' )
	print( "───> BIENVENIDO A BASE DE DATOS ESCUELA CONDUCCION SEVILLA <───\n" )
	while intentos != 0:
		usuario = input( "Digite el usuario: " )
		password = getpass.getpass( "Digite la contraseña: " )
		try:
			if password == secretarias[ usuario ][ 0 ]:
				nombreSecretaria = secretarias[ usuario ][ 1 ]
				print( f"\nHas ingresado correctamente, Bienvenid@ { nombreSecretaria }" )
				time.sleep( 1.5 )
				os.system( 'cls' )
				return nombreSecretaria
			else:
				intentos -= 1
				print( "\nDatos erroneos intentalo de nuevo" )
				print( f"Intentos Restantes: { intentos }\n" )
		except KeyError:
			intentos -= 1
			print( "\nDatos erroneos intentalo de nuevo" )
			print( f"Intentos Restantes: { intentos }\n" )
	exit()
