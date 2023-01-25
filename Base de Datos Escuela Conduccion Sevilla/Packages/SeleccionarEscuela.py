from Packages.Menus import menuSeleccionEscuela
from Packages.Funciones import preguntarNumero, guardarArchivoDatos
from Packages.Escuela import escuela
from Packages.Ajustes import ajustes

import marshal
import os
import os.path as path

def seleccionarEscuela( nombreSecretaria ):
    while True:
        menuSeleccionEscuela( nombreSecretaria )
        opcionMenuSelccionEscuela = preguntarNumero( 0, 3, "[0,1,2,3]" )
        os.system( 'cls' )
        if opcionMenuSelccionEscuela == 1: #Sevilla ( Caicedonia )
            contenidoSevilla = {}
            if path.exists( "Datos/datosSevilla" ):
                archivo = open( f"Datos/datosSevilla/datosSevilla", "br" )
                contenidoSevilla = marshal.load( archivo )
                archivo.close()
            else:
                os.mkdir( "Datos/datosSevilla" )
                guardarArchivoDatos( contenidoSevilla, "datosSevilla" )
            escuela( contenidoSevilla, "datosSevilla", nombreSecretaria )
        elif opcionMenuSelccionEscuela == 2: #Sevilla 1
            contenidoSevilla1 = {}
            if path.exists( "Datos/DatosSevilla1" ):
                archivo = open( f"Datos/datosSevilla1/datosSevilla1", "br" )
                contenidoSevilla1 = marshal.load( archivo )
                archivo.close()
            else:
                os.mkdir( "Datos/datosSevilla1" )
                guardarArchivoDatos( contenidoSevilla1, "datosSevilla1" )
            escuela( contenidoSevilla1, "datosSevilla1", nombreSecretaria )
        elif opcionMenuSelccionEscuela == 3: #Ajustes
            ajustes( nombreSecretaria )
        elif opcionMenuSelccionEscuela == 0:
            print( "Hasta pronto" )
            return