from Packages.Menus import menuBuscarPor
from Packages.Funciones import preguntarNumero

import os

def imprimirUsuario( usuario ):
    print( f"""Nombre: { usuario[ 0 ] }
 Cedula: { usuario[ 1 ] }
 Telefono: { usuario[ 2 ] }
 Correo: { usuario[ 3 ] }
 Categoria: { usuario[ 5 ] }
 Precio Examen Medico: ${ usuario[ 6 ] }
 Precio Lamina: ${ usuario[ 7 ] }
 Precio Curso: ${ usuario[ 8 ] }
 Precio Total a Pagar: ${ usuario [ 10 ] } + ${ usuario[ 6 ] } + ${ usuario[ 7 ] } = ${ usuario [ 10 ] + usuario[ 6 ] + usuario[ 7 ] }
 Fecha Registro: { usuario[ 4 ][ 0 ] } / { usuario[ 4 ][ 1 ] } / { usuario[ 4 ][ 2 ] }""" )
    if len( usuario[ 9 ] ) == 0:
        print( " Abonos: Ninguno" )
    else:
        print( " Abonos: " )
        for i in range( len( usuario[ 9 ] ) ):
            print( f"  ${ usuario[ 9 ][ i ][ 0 ] } - Realizado por { usuario[ 9 ][ i ][ 2 ] } el { usuario[ 9 ][ i ][ 1 ] }" )

def imprimirUsuarioSeguro( nombre, cedula, telefono, correo, categoria ):
        print( f"""Nombre: { nombre }
 Cedula: { cedula }
 Telefono: { telefono }
 Correo: { correo }
 Categoria: { categoria }""" )

def buscarUsuarioPorNombre( datosEscuela ):
    if len( datosEscuela ) == 0:
        print( "\nBase de datos vacia\n" )
    else:
        encontroUsuario = False
        print( "───> BASE DE DATOS ESCUELA CONDUCCION SEVILLA BUSCAR POR NOMBRE <───\n" )
        nombreParaBuscar = input( "───> Digite el nombre a buscar: " )
        print()
        for cedula in datosEscuela:
            if datosEscuela[ cedula ][ 0 ].lower().find( nombreParaBuscar.lower() ) != -1:
                imprimirUsuario( datosEscuela[ cedula ] )
                encontroUsuario = True
                print()
        if not encontroUsuario:
            print( f"No se ha encontrado ningun usuario con Nombre '{ nombreParaBuscar }'\n" )

def buscarUsuarioPorCedula( datosEscuela ):
    if len( datosEscuela ) == 0:
        print( "\nBase de datos vacia\n" )
    else:
        print( "───> BASE DE DATOS ESCUELA CONDUCCION SEVILLA BUSCAR POR CEDULA <───\n" )
        cedulaParaBuscar = input( "───> Digite la cedula a buscar: " )
        try:
            print()
            imprimirUsuario( datosEscuela[ cedulaParaBuscar ] )
            print()
        except KeyError:
            print( f"No se encuentra ningun usuario con Cedula '{ cedulaParaBuscar }'\n" )

def buscarUsuarioPorCategoria( datosEscuela ):
    if len( datosEscuela ) == 0:
        print( "\nBase de datos vacia\n" )
    else:
        encontroUsuario = False
        print( "───> BASE DE DATOS ESCUELA CONDUCCION SEVILLA BUSCAR POR CATEGORIA <───\n" )
        print( """Categorias Disponibles a buscar:

    1. A2
    2. B1
    3. C1
    4. A2 y B1
    5. A2 y C1
    6. A2 y Refrendacion B1
    7. A2 y Refrendacion C1
    8. B1 y Refrendacion A2
    9. C1 y Refrendacion A2""")
        categoriaParaBuscar = preguntarNumero( 1, 9, "[1,2,3,4,5,6,7,8,9]" )
        if categoriaParaBuscar  == 1:
            categoria = "A2"
        elif categoriaParaBuscar  == 2:
            categoria = "B1"
        elif categoriaParaBuscar  == 3:
            categoria = "C1"
        elif categoriaParaBuscar  == 4:
            categoria = "A2 y B1"
        elif categoriaParaBuscar  == 5:
            categoria = "A2 y C1"
        elif categoriaParaBuscar == 6:
            categoria = "A2 y Refrendacion B1"  
        elif categoriaParaBuscar == 7:
            categoria = "A2 y Refrendacion C1"
        elif categoriaParaBuscar == 8:
            categoria = "B1 y Refrendacion A2"  
        elif categoriaParaBuscar == 9:
            categoria = "C1 y Refrendacion A2"
        for cedula in datosEscuela:
            if datosEscuela[ cedula ][ 5 ] == categoria:
                imprimirUsuario( datosEscuela[ cedula ] )
                encontroUsuario = True
                print()
        if not encontroUsuario:
            print( f"No se ha encontrado ningun usuario con Categoria '{ categoria }'\n" )

def buscarUsuarioPorCorreo( datosEscuela ):
    if len( datosEscuela ) == 0:
        print( "\nBase de datos vacia\n" )
    else:
        encontroUsuario = False
        print( "───> BASE DE DATOS ESCUELA CONDUCCION SEVILLA BUSCAR POR CORREO <───\n" )
        correoParaBuscar = input( "───> Digite el correo a buscar: " )
        print()
        for cedula in datosEscuela:
            if datosEscuela[ cedula ][ 3 ] == correoParaBuscar:
                imprimirUsuario( datosEscuela[ cedula ] )
                encontroUsuario = True
                print()
        if not encontroUsuario:
            print( f"No se ha encontrado ningun usuario con Correo '{ correoParaBuscar }'\n" )

def buscarUsuarioPorTelefono( datosEscuela ):
    if len( datosEscuela ) == 0:
        print( "\nBase de datos vacia\n" )
    else:
        encontroUsuario = False
        print( "───> BASE DE DATOS ESCUELA CONDUCCION SEVILLA BUSCAR POR TELEFONO <───\n" )
        telefonoParaBuscar = input( "───> Digite el telefono a buscar: " )
        print()
        for cedula in datosEscuela:
            if datosEscuela[ cedula ][ 2 ] == telefonoParaBuscar:
                imprimirUsuario( datosEscuela[ cedula ] )
                encontroUsuario = True
                print()
        if not encontroUsuario:
            print( f"No se ha encontrado ningun usuario con Telefono '{ telefonoParaBuscar }'\n" )

def buscarUsuarioPorMes( datosEscuela ):
    if len( datosEscuela ) == 0:
        print( "\nBase de datos vacia\n" )
    else:
        encontroUsuario = False
        print( "───> BASE DE DATOS ESCUELA CONDUCCION SEVILLA BUSCAR POR MES <───\n" )
        print("""Meses:

1. Enero
2. Febrero
3. Marzo
4. Abril
5. Mayo
6. Junio
7. Julio
8. Agosto
9. Septiembre
10. Octubre
11. Noviembre
12. Diciembre""")
        mesParaBuscar = preguntarNumero( 1, 12, "[1,2,3,4,5,6,7,8,9,10,11,12]")
        for cedula in datosEscuela:
            if datosEscuela[ cedula ][ 4 ][ 1 ] == mesParaBuscar:
                imprimirUsuario( datosEscuela[ cedula ] )
                encontroUsuario = True
                print()
        if not encontroUsuario:
            print( f"No se ha encontrado ningun usuario registrado en el mes '{ mesParaBuscar }'\n" )


def buscarUsuarioPorFaltantesPago( datosEscuela ):
    if len( datosEscuela ) == 0:
        print( "\nBase de datos vacia\n" )
    else:
        encontroUsuario = False
        print( "───> BASE DE DATOS ESCUELA CONDUCCION SEVILLA BUSCAR FALTANTES PAGOS <───\n" )
        for cedula in datosEscuela:
            if datosEscuela[ cedula ][ 10 ] != 0:
                imprimirUsuario( datosEscuela[ cedula ] )
                encontroUsuario = True
                print()
        if not encontroUsuario:
            print( f"No se ha encontrado ningun usuario que debe dinero\n" )

def mostrarTodosLosUsuarios( datosEscuela ):
    if len( datosEscuela ) == 0:
        print( "\nBase de datos vacia\n" )
    else:
        print( f"\nUsuarios Registrados { len( datosEscuela ) }:\n")
        for cedula in datosEscuela:
            imprimirUsuario( datosEscuela[ cedula ] )
            print()

def buscarUsuarioPor( datosEscuela, nombreSecretaria ):
    while True:
        menuBuscarPor( nombreSecretaria )
        opcionBuscarPor = preguntarNumero( 0, 8, "[0,1,2,3,4,5,6,7,8]" )
        os.system( 'cls' )
        if opcionBuscarPor == 1:
            buscarUsuarioPorNombre( datosEscuela )
        elif opcionBuscarPor == 2:
            buscarUsuarioPorCedula( datosEscuela )
        elif opcionBuscarPor == 3:
            buscarUsuarioPorCategoria( datosEscuela )
        elif opcionBuscarPor == 4:
            buscarUsuarioPorCorreo( datosEscuela )
        elif opcionBuscarPor == 5:
            buscarUsuarioPorTelefono( datosEscuela )
        elif opcionBuscarPor == 6:
            buscarUsuarioPorMes( datosEscuela )
        elif opcionBuscarPor == 7:
            buscarUsuarioPorFaltantesPago( datosEscuela )
        elif opcionBuscarPor == 8:
            mostrarTodosLosUsuarios( datosEscuela )
        elif opcionBuscarPor == 0:
            return