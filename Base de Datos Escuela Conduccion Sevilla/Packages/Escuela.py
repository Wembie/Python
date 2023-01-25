from Packages.Menus import menuEscuela, menuEditarUsuario
from Packages.Funciones import preguntarNumero, guardarArchivoDatos, preguntarNumeroNormal, enviarCorreo
from Packages.BuscarPor import buscarUsuarioPor, imprimirUsuarioSeguro, imprimirUsuario
from datetime import datetime

import os
import json

with open( "Datos/preciosEscuela.json" ) as archivo:
    preciosEscuela = json.load( archivo )

A2 = preciosEscuela[ 'A2' ]
B1 = preciosEscuela[ 'B1' ]
C1 = preciosEscuela[ 'C1' ]
LaminaUnaCategoria = preciosEscuela[ 'Lamina1' ]
ExamenMedicoUnaCategoria = preciosEscuela[ 'Examen1' ]
A2_B1 = preciosEscuela[ 'A2_B1' ]
A2_C1 = preciosEscuela[ 'A2_C1' ] 
LaminaDosCategoria = preciosEscuela[ 'Lamina2' ]
ExamenMedicoDosCategoria = preciosEscuela[ 'Examen2' ]

def name( pregunta ):
    nombre = input( f"Digite el nombre del usuario a { pregunta }: " )
    nombreSeparado = nombre.split()
    nombreBonito = ""
    for i in range( len( nombreSeparado ) ):
        mayuscula = True
        for letra in nombreSeparado[ i ]:
            if mayuscula:
                nombreBonito += letra.upper()
                mayuscula = False
            else:
                nombreBonito += letra.lower()
        if len( nombreSeparado ) - 1 != i:
            nombreBonito += " "
        else:
            nombreBonito += ""
    return nombreBonito

def registrarUsuario( datosEscuela, nombreArchivo, nombreSecretaria ):
    while True:
        print( "───> BASE DE DATOS ESCUELA CONDUCCION SEVILLA AGREGAR USUARIO <───\n" )
        nombre = name( "registar" )
        while True:
            cedula = preguntarNumeroNormal( f"Digite la cedula de { nombre }: ", 4 )
            cedula = str( cedula )
            if cedula in datosEscuela:
                print( "\nUsuario ya registrado\n" )
            else:
                break
        #telefono = preguntarNumeroNormal( f"Digite el telefono de { nombre }: ", 4 )
        #telefono = str( telefono )
        telefono = "-"
        #while True:
            #correo = input( f"Digite el correo de { nombre }: " )
            #correoValido = False
            #cantidadArrobas = 0
            #for letra in correo:
                #if letra == "@":
                    #correoValido = True
                    #cantidadArrobas += 1
            #if correoValido and cantidadArrobas == 1:
                #break
            #else:
                #print( "\nCorreo invalido digitalo nuevamente\n" )         
        #correo = correo.lower()
        correo = "-"
        print( """Categorias Disponibles:

    1. A2
    2. B1
    3. C1
    4. A2 y B1
    5. A2 y C1
    6. A2 y Refrendacion B1
    7. A2 y Refrendacion C1
    8. B1 y Refrendacion A2
    9. C1 y Refrendacion A2""")
        categoria = preguntarNumero( 1, 9, "[1,2,3,4,5,6,7,8.9]" )
        if categoria == 1:
            categoria = "A2"
            precio = A2
            lamina = LaminaUnaCategoria
            examenMedico = ExamenMedicoUnaCategoria
        elif categoria == 2:
            categoria = "B1"
            precio = B1
            lamina = LaminaUnaCategoria
            examenMedico = ExamenMedicoUnaCategoria
        elif categoria == 3:
            categoria = "C1"
            precio = C1
            lamina = LaminaUnaCategoria
            examenMedico = ExamenMedicoUnaCategoria
        elif categoria == 4:
            categoria = "A2 y B1"
            precio = A2_B1
            lamina = LaminaDosCategoria
            examenMedico = ExamenMedicoDosCategoria
        elif categoria == 5:
            categoria = "A2 y C1"
            precio = A2_C1
            lamina = LaminaDosCategoria
            examenMedico = ExamenMedicoDosCategoria
        elif categoria == 6:
            categoria = "A2 y Refrendacion B1"
            precio = A2
            lamina = LaminaDosCategoria
            examenMedico = ExamenMedicoDosCategoria     
        elif categoria == 7:
            categoria = "A2 y Refrendacion C1"
            precio = A2
            lamina = LaminaDosCategoria
            examenMedico = ExamenMedicoDosCategoria  
        elif categoria == 8:
            categoria = "B1 y Refrendacion A2"
            precio = B1
            lamina = LaminaDosCategoria
            examenMedico = ExamenMedicoDosCategoria     
        elif categoria == 9:
            categoria = "C1 y Refrendacion A2"
            precio = C1
            lamina = LaminaDosCategoria
            examenMedico = ExamenMedicoDosCategoria    
        print( "Datos Registrados Anteriormente: \n")
        imprimirUsuarioSeguro( nombre, cedula, telefono, correo, categoria )
        print( """\nEstas Seguro de que toda la informacion que digitaste esta correcta?

0. No
1. Si""" )
        estasSeguro = preguntarNumero( 0, 1, "[0,1]" )
        if estasSeguro:
            fecha = datetime.now()
            datosEscuela[ cedula ] = [ nombre, cedula, telefono, correo, [ fecha.day, fecha.month, fecha.year ] , categoria, examenMedico, lamina, precio, [], precio ]
            mensaje = f"""Nuevo Usuario Registrado por: { nombreSecretaria }

Datos Registrados:

Fecha de Registro: { fecha.day } / { fecha.month } / { fecha.year }
Nombre: { nombre }
Cedula: { cedula }
Telefono: { telefono }
Correo: { correo }
Categoria: { categoria }
Precio Examen Medico: ${ examenMedico }
Precio Lamina: ${ lamina }
Precio Curso: ${ precio }
Precio Total a Pagar: ${ precio }"""
            #enviarCorreo( "Nuevo Usuario Registrado", mensaje )
            guardarArchivoDatos( datosEscuela, nombreArchivo )
            print( f"{ nombre } ha sido registrado con exito!\n" )
            break
        else:
            print( "Digita nuevamente la informacion solicitada\n")

def editarUsuario( datosEscuela, nombreArchivo ):
    def editarNombre( datosEscuela, cedula ):
        nombre = name( "editar" )
        datosEscuela[ cedula ][ 0 ] = nombre

    def editarCedula( datosEscuela, cedulaParaBuscar ):
        while True:
            cedula = preguntarNumeroNormal( f"Digite la cedula a editar: ", 4 )
            cedula = str( cedula )
            if cedula in datosEscuela:
                print( "\nUsuario ya registrado\n" )
            else:
                break
        datosEscuela[ cedulaParaBuscar ][ 1 ] = cedula
        datosEscuela[ cedula ] = datosEscuela[ cedulaParaBuscar ]
        del datosEscuela[ cedulaParaBuscar ]
        return cedula

    def editarTelefono( datosEscuela, cedula ):
        telefono = preguntarNumeroNormal( f"Digite el telefono a editar: ", 4 )
        telefono = str( telefono )
        datosEscuela[ cedula ][ 2 ] = telefono

    def editarCorreo( datosEscuela, cedula ):
        while True:
            correo = input( f"Digite el correo a editar: " )
            correoValido = False
            cantidadArrobas = 0
            for letra in correo:
                if letra == "@":
                    correoValido = True
                    cantidadArrobas += 1
            if correoValido and cantidadArrobas == 1:
                break
            else:
                print( "\nCorreo invalido digitalo nuevamente\n" )         
        correo = correo.lower()
        datosEscuela[ cedula ][ 3 ] = correo

    def editarCategoria( datosEscuela, cedula ):
        print( """Recuerda si editas la categoria y la persona ya tiene abonos, se retiraran, es decir, quedara como nuevo totalmente.
        
Categorias Disponibles a editar:

    1. A2
    2. B1
    3. C1
    4. A2 y B1
    5. A2 y C1
    6. A2 y Refrendacion B1
    7. A2 y Refrendacion C1
    8. B1 y Refrendacion A2
    9. C1 y Refrendacion A2""")
        categoria = preguntarNumero( 1, 9, "[1,2,3,4,5,6,7,8,9]" )
        if categoria == 1:
            categoria = "A2"
            precio = A2
            lamina = LaminaUnaCategoria
            examenMedico = ExamenMedicoUnaCategoria
        elif categoria == 2:
            categoria = "B1"
            precio = B1
            lamina = LaminaUnaCategoria
            examenMedico = ExamenMedicoUnaCategoria
        elif categoria == 3:
            categoria = "C1"
            precio = C1
            lamina = LaminaUnaCategoria
            examenMedico = ExamenMedicoUnaCategoria
        elif categoria == 4:
            categoria = "A2 y B1"
            precio = A2_B1
            lamina = LaminaDosCategoria
            examenMedico = ExamenMedicoDosCategoria
        elif categoria == 5:
            categoria = "A2 y C1"
            precio = A2_C1
            lamina = LaminaDosCategoria
            examenMedico = ExamenMedicoDosCategoria
        elif categoria == 6:
            categoria = "A2 y Refrendacion B1"
            precio = A2
            lamina = LaminaDosCategoria
            examenMedico = ExamenMedicoDosCategoria     
        elif categoria == 7:
            categoria = "A2 y Refrendacion C1"
            precio = A2
            lamina = LaminaDosCategoria
            examenMedico = ExamenMedicoDosCategoria  
        elif categoria == 8:
            categoria = "B1 y Refrendacion A2"
            precio = B1
            lamina = LaminaDosCategoria
            examenMedico = ExamenMedicoDosCategoria     
        elif categoria == 9:
            categoria = "C1 y Refrendacion A2"
            precio = C1
            lamina = LaminaDosCategoria
            examenMedico = ExamenMedicoDosCategoria 
        datosEscuela[ cedula ][ 5 ] = categoria
        datosEscuela[ cedula ][ 6 ] = examenMedico 
        datosEscuela[ cedula ][ 7 ] = lamina
        datosEscuela[ cedula ][ 8 ] = precio
        datosEscuela[ cedula ][ 9 ] = []
        datosEscuela[ cedula ][ 10 ] = precio

    def editarAbonos( datosEscuela, cedula ):
        if len( datosEscuela[ cedula ][ 9 ] ) == 0:
            print( "No hay abonos a editar" )
        else:
            while True:
                abonosRealizados = datosEscuela[ cedula ][ 9 ]
                print( "Abonos encontrados:\n" )
                for i in range( len( abonosRealizados ) ):
                    print( f"{ i + 1 }. ${ abonosRealizados[ i ][ 0 ] } - Realizado por { abonosRealizados[ i ][ 2 ] } el { abonosRealizados[ i ][ 1 ] }" )
                print( "0. Volver" )
                opcionEditarAbono = preguntarNumero( 0, len( abonosRealizados ), "de abono a borrar" )
                if opcionEditarAbono == 0:
                    break
                else:
                    print( f"Borraste el abono #{ opcionEditarAbono } con exito y se le sumo un total de: ${ abonosRealizados[ opcionEditarAbono - 1 ][ 0 ] }, total restante: ${ datosEscuela[ cedula ][ 10 ] + datosEscuela[ cedula ][ 9 ][ opcionEditarAbono - 1 ][ 0 ] }\n")
                    datosEscuela[ cedula ][ 10 ] += datosEscuela[ cedula ][ 9 ][ opcionEditarAbono - 1 ][ 0 ]
                    abonosRealizados.pop( opcionEditarAbono - 1 )
                if len( abonosRealizados ) == 0:
                    datosEscuela[ cedula ][ 9 ] = []
                    break

    def editarPrecio( datosEscuela, cedula ): #Descuenticos del Fernando
        if len( datosEscuela[ cedula ][ 9 ] ) == 0 :
            print( "Si te equivocaste cierra la aplicacion y vuelve a abrirla.\n" )
            print( "Descuenticos Fernando:\n" )
            while True:
                precio = preguntarNumeroNormal( "Digite el valor que Fernando le dijo al cliente: $", 2 )
                if isinstance( datosEscuela[ cedula ][ 8 ], int ):
                    if datosEscuela[ cedula ][ 8 ] - precio < 0:
                        print( "\nNo puede quedar salgo negativo, intentalo de nuevo\n" )
                    else:
                        datosEscuela[ cedula ][ 8 ] = str( datosEscuela[ cedula ][ 8 ] ) + " - $" + str( datosEscuela[ cedula ][ 8 ] - precio ) + " Descuento"
                        break
                elif isinstance( datosEscuela[ cedula ][ 8 ], str ):
                    curso = datosEscuela[ cedula ][ 8 ].split()
                    curso = int( curso[ 0 ] )
                    if curso - precio < 0:
                        print( "\nNo puede quedar salgo negativo, intentalo de nuevo\n" )
                    else:
                        datosEscuela[ cedula ][ 8 ] = str( curso ) + " - $" + str( curso - precio ) + " Descuento"
                        break                    
            datosEscuela[ cedula ][ 10 ] = precio
        else:
            print( "\nNo se puede editar el precio si ya hay abonos\n")

    if len( datosEscuela ) == 0:
        print( "\nBase de datos vacia\n" )
    else:
        print( "───> BASE DE DATOS ESCUELA CONDUCCION SEVILLA EDITAR USUARIO <───\n" )
        cedulaParaBuscar = input( "───> Digite la cedula a realizar ediccion de usuario: " )
        os.system( 'cls' )
        try:
            while True:
                print( "───> BASE DE DATOS ESCUELA CONDUCCION SEVILLA EDITAR USUARIO <───\n" )
                imprimirUsuario( datosEscuela[ cedulaParaBuscar ] )
                menuEditarUsuario()
                opcionMenuEditarUsuario = preguntarNumero( 0, 7, "[0,1,2,3,4,5,6,7]" )
                if opcionMenuEditarUsuario == 1:
                    editarNombre( datosEscuela, cedulaParaBuscar )
                elif opcionMenuEditarUsuario == 2:
                    cedulaParaBuscar = editarCedula( datosEscuela, cedulaParaBuscar )
                elif opcionMenuEditarUsuario == 3:
                    editarTelefono( datosEscuela, cedulaParaBuscar )
                elif opcionMenuEditarUsuario == 4:
                    editarCorreo( datosEscuela, cedulaParaBuscar )
                elif opcionMenuEditarUsuario == 5:
                    editarCategoria( datosEscuela, cedulaParaBuscar )
                elif opcionMenuEditarUsuario == 6:
                    editarAbonos( datosEscuela, cedulaParaBuscar )
                elif opcionMenuEditarUsuario == 7:
                    editarPrecio( datosEscuela, cedulaParaBuscar )
                elif opcionMenuEditarUsuario == 0:
                    os.system( 'cls' )
                    break
                os.system( 'cls' )
            guardarArchivoDatos( datosEscuela, nombreArchivo )
        except KeyError:
            print( f"No se encuentra ningun usuario con Cedula '{ cedulaParaBuscar }'\n" )

def realizarPagoUsuario( datosEscuela, nombreArchivo, nombreSecretaria ):
    if len( datosEscuela ) == 0:
        print( "\nBase de datos vacia\n" )
    else:
        fecha = datetime.now()
        fecha = f"{ fecha.day } / { fecha.month } / { fecha.year }"
        print( "───> BASE DE DATOS ESCUELA CONDUCCION SEVILLA REALIZAR PAGO <───\n" )
        cedulaParaBuscar = input( "───> Digite la cedula a realizar abono: " )
        try:
            if datosEscuela[ cedulaParaBuscar ][ 10 ] == 0:
                print( f"\n{ datosEscuela[ cedulaParaBuscar ][ 0 ] }, ya esta a paz y salvo\n")
            else:
                print()
                print( f"Total Restante de { datosEscuela[ cedulaParaBuscar ][ 0 ] }: ${ datosEscuela[ cedulaParaBuscar ][ 10 ] }\n")
                while True:
                    abono = preguntarNumeroNormal( f"Cuanto desea abonar para { datosEscuela[ cedulaParaBuscar ][ 0 ] }: $", 0 )
                    if datosEscuela[ cedulaParaBuscar ][ 10 ] - abono < 0:
                        print( "\nPagaste de mas, intentalo de nuevo\n" )
                    elif datosEscuela[ cedulaParaBuscar ][ 10 ] - abono >= 0:
                        break
                datosEscuela[ cedulaParaBuscar ][ 9 ].append( [ abono, fecha, nombreSecretaria ] )
                datosEscuela[ cedulaParaBuscar ][ 10 ] -= abono
                mensaje = f"""Nuevo Abono Realizado por: { nombreSecretaria }

Datos del Abono:

Fecha del Abono: { fecha }
Nombre: { datosEscuela[ cedulaParaBuscar ][ 0 ] }
Cedula: { datosEscuela[ cedulaParaBuscar ][ 1 ] }
Telefono: { datosEscuela[ cedulaParaBuscar ][ 2 ] }
Correo: { datosEscuela[ cedulaParaBuscar ][ 3 ] }
Categoria: { datosEscuela[ cedulaParaBuscar ][ 5 ] }
Precio Curso: ${ datosEscuela[ cedulaParaBuscar ][ 8 ] }
Precio Abonado: ${ abono }
Precio Total restante: ${ datosEscuela[ cedulaParaBuscar ][ 10 ] }"""
                #enviarCorreo( "Nuevo Abono Registrado", mensaje )
                guardarArchivoDatos( datosEscuela, nombreArchivo )
                print( f"\nAbono de ${ abono } realizado con exito a { datosEscuela[ cedulaParaBuscar ][ 0 ] }, resta: ${ datosEscuela[ cedulaParaBuscar ][ 10 ] }\n" )
        except KeyError:
            print( f"\nNo se encuentra ningun usuario con Cedula '{ cedulaParaBuscar }'\n" )
     
def escuela( datosEscuela, nombre, nombreSecretaria ):
    while True:
        menuEscuela( nombreSecretaria )
        opcionMenuEscuela = preguntarNumero( 0, 4, "[0,1,2,3,4]" )
        os.system( 'cls' )
        if opcionMenuEscuela == 1:
            registrarUsuario( datosEscuela, nombre, nombreSecretaria )
        elif opcionMenuEscuela == 2:
            editarUsuario( datosEscuela, nombre )
        elif opcionMenuEscuela == 3:
            realizarPagoUsuario( datosEscuela, nombre, nombreSecretaria )
        elif opcionMenuEscuela == 4:
            buscarUsuarioPor( datosEscuela, nombreSecretaria )
        elif opcionMenuEscuela == 0:
            return