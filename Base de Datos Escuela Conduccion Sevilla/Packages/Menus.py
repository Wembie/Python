def menuSeleccionEscuela( nombreSecretaria ):
    print( f"""───> BASE DE DATOS ESCUELA CONDUCCION SEVILLA <───

Secretari@: { nombreSecretaria }

1. Sevilla ( Caicedonia )
2. Seviila 1
3. Ajustes ( ADMIN )
0. Salir""" )
    
def menuEscuela( nombreSecretaria ):
    print( f"""───> MENU BASE DE DATOS ESCUELA CONDUCCION SEVILLA <───

Secretari@: { nombreSecretaria }

1. Registrar Usuario
2. Editar Usuario 
3. Realizar Pago Usuario
4. Buscar Usuario por...
0. Volver""" )

def menuBuscarPor( nombreSecretaria ):
    print( f"""───> MENU BASE DE DATOS ESCUELA CONDUCCION SEVILLA BUSCAR POR <───

Secretari@: { nombreSecretaria }

1. Buscar Usuario por Nombre
2. Buscar Usuario por Cedula
3. Buscar Usuario por Categoria
4. Buscar Usuario por Correo
5. Buscar Usuario por Telefono
6. Buscar Usuarios por Mes
7. Buscar Usuarios Faltantes por Pagar
8. Mostrar Todos los Usuarios
0. Volver""" ) 

def menuAjustes( nombreSecretaria ):
    print( f"""───> MENU BASE DE DATOS ESCUELA CONDUCCION AJUSTES <───

Secretari@: { nombreSecretaria }

1. Editar Precios
0. Actualizar Ajustes Realizados""" ) 

def menuEditarUsuario():
    print( f"""\n1. Editar Nombre
2. Editar Cedula
3. Editar Telefono
4. Editar Correo
5. Editar Categoria
6. Borrar Abonos
7. Editar Precio (Descuentos)
0. Volver""" ) 