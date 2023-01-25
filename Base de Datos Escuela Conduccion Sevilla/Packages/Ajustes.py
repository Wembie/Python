from Packages.Menus import menuAjustes
from Packages.Funciones import preguntarNumero, preguntarNumeroNormal, espera

import os
import json
import time
import subprocess

with open( "Datos/preciosEscuela.json" ) as archivo:
    preciosEscuela = json.load( archivo )

def precios():
    def editarPrecio( llave, nombre ):
        print( f"Precio Actual: ${ preciosEscuela[ llave ] }\n" )
        precio = preguntarNumeroNormal( f"Digite el nuevo precio de { nombre }: $", 4 )
        preciosEscuela[ llave ] = precio

    while True:
        print( f"""───> BASE DE DATOS ESCUELA CONDUCCION SEVILLA AJUSTES : PRECIOS <───

1. Editar Precio A2 - Actual: ${ preciosEscuela[ 'A2' ] }
2. Editar Precio B1 - Actual: ${ preciosEscuela[ 'B1' ] }
3. Editar Precio C1 - Actual: ${ preciosEscuela[ 'C1' ] }
4. Editar Precio A2 y B1 - Actual: ${ preciosEscuela[ 'A2_B1' ] }
5. Editar Precio A2 y C1 - Actual: ${ preciosEscuela[ 'A2_C1' ] }
6. Editar Precio Lamina Para '1' Categoria - Actual: ${ preciosEscuela[ 'Lamina1' ] }
7. Editar Precio Lamina Para '2' Categorias - Actual: ${ preciosEscuela[ 'Lamina2' ] }
8. Editar Precio Examen Medico Para '1' Categoria - Actual: ${ preciosEscuela[ 'Examen1' ] }
9. Editar Precio Examen Medico Para '2' Categorias - Actual: ${ preciosEscuela[ 'Examen2' ] }
10. Editar Todos Los Precios
0. Volver""" )
        opcionMenuEditarPrecios = preguntarNumero( 0, 10, "[0,1,2,3,4,5,6,7,8,9,10]" )
        if opcionMenuEditarPrecios == 1:
            editarPrecio( 'A2', "A2" )
        elif opcionMenuEditarPrecios == 2:
            editarPrecio( 'B1', "B1" )
        elif opcionMenuEditarPrecios == 3:
            editarPrecio( 'C1', "C1" )
        elif opcionMenuEditarPrecios == 4:
            editarPrecio( 'A2_B1', "A2 y B1" )
        elif opcionMenuEditarPrecios == 5:
            editarPrecio( 'A2_C1', "A2 y C1" )
        elif opcionMenuEditarPrecios == 6:
            editarPrecio( 'Lamina1', "Lamina Para '1' Categoria" )
        elif opcionMenuEditarPrecios == 7:
            editarPrecio( 'Lamina2', "Lamina Para '2' Categorias" )
        elif opcionMenuEditarPrecios == 8:
            editarPrecio( 'Examen1', "Examen Medico Para '1' Categoria" )
        elif opcionMenuEditarPrecios == 9:
            editarPrecio( 'Examen2', "Examen Medico Para '2' Categorias" )
        elif opcionMenuEditarPrecios == 10:
            editarPrecio( 'A2', "A2" )
            editarPrecio( 'B1', "B1" )
            editarPrecio( 'C1', "C1" )
            editarPrecio( 'A2_B1', "A2 y B1" )
            editarPrecio( 'A2_C1', "A2 y C1" )
            editarPrecio( 'Lamina1', "Lamina Para '1' Categoria" )
            editarPrecio( 'Lamina2', "Lamina Para '2' Categorias" )
            editarPrecio( 'Examen1', "Examen Medico Para '1' Categoria" )
            editarPrecio( 'Examen2', "Examen Medico Para '2' Categorias" )
        elif opcionMenuEditarPrecios == 0:
            os.system( 'cls' )
            return
        os.system( 'cls' )
        
def ajustes( nombreSecretaria ):
    while True:
        menuAjustes( nombreSecretaria )
        opcionMenuAjustes = preguntarNumero( 0, 1, "[0,1]" )
        os.system( 'cls' )
        if opcionMenuAjustes == 1: #Precios
            precios()
        elif opcionMenuAjustes == 0:
            with open( "Datos/preciosEscuela.json", 'w' ) as archivoNuevo:
                json.dump( preciosEscuela, archivoNuevo, indent = 4 )
            espera( "Actualizando Ajustes" )
            print( "\n\nAjustes Actualizados\n" )
            time.sleep( 1.5 ) 
            espera( "Reiniciando Aplicacion" )
            os.system( 'cls' )
            subprocess.run( [ "python", "main.py" ] ) #Reinicio
            exit()