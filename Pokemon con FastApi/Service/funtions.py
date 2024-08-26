from fastapi import HTTPException, status

import marshal
import os
import requests
import logging

logging.basicConfig( level = logging.INFO, format ='%(asctime)s - %(levelname)s - %(message)s' )

logger = logging.getLogger( __name__ )

def guardar( datos ):
        archivo = open( "Datos/datosBatallas", "bw" )
        marshal.dump( datos, archivo )
        archivo.close()

def cargar():
    datosBatallas = {}
    if os.path.exists( "Datos/datosBatallas" ):
        archivo = open( f"Datos/datosBatallas", "br" )
        datosBatallas = marshal.load( archivo )
        archivo.close()
    else:
        guardar( datosBatallas )
    return datosBatallas

def extraer( nombrePokemon ):
    url = 'https://pokeapi.co/api/v2/pokemon/'
    respuesta = requests.get( url + nombrePokemon.lower() )
    if respuesta.status_code == 200:
        datosPokemon = respuesta.json()
        return {
            'name': datosPokemon[ 'name' ],
        **{ stat[ 'stat' ][ 'name' ] : stat[ 'base_stat' ] for stat in datosPokemon[ 'stats' ] }
    }
    #respuesta.status_code
    raise HTTPException( status_code = status.HTTP_404_NOT_FOUND, detail = f"Pokemon { nombrePokemon } not found" )
    
def imprimirStats( pokemon ):
    logger.info( f"""Nombre: { pokemon[ 'name' ] }
Vida: { pokemon[ 'hp' ] }
Ataque: { pokemon[ 'attack' ] }
Defensa: { pokemon[ 'defense' ] }
Velocidad: { pokemon[ 'speed' ] }""" )