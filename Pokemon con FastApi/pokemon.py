from fastapi import FastAPI
from Models.models import Battle, Battle_Result
from Service.funtions import cargar, guardar, extraer, logger
from Service.emulateBattle import pelear

app = FastAPI()

@app.post( "/pokemon-battle" )
def pokemon_battle( battle : Battle ):  
    datosBatallas = cargar() 
    pokemonA = extraer( battle.pokemon_name_1 )
    pokemonB = extraer( battle.pokemon_name_2 )
    if pokemonA[ 'name' ] == pokemonB[ 'name' ]:
        pokemonA[ 'name' ] += "1"
        pokemonB[ 'name' ] += "2"
    if f"{ pokemonA[ 'name' ] }-{ pokemonB[ 'name' ] }" in datosBatallas or f"{ pokemonB[ 'name' ] }-{ pokemonA[ 'name' ] }" in datosBatallas:
        logger.info( "La batalla ya se encontraba en nuestros registros..." )
        if pokemonA[ 'speed' ] == pokemonB[ 'speed' ]:
            logger.info( f"ACLARANDO COMO TIENEN LA MISMA VELOCIDAD EN ESTA OCASION EL INICIADOR FUE: { datosBatallas[ f"{ pokemonA[ 'name' ] }-{ pokemonB[ 'name' ] }" ][ 1 ].upper() }" )
        logger.info( f"El ganador de la batalla pokemon de { pokemonA[ 'name' ] } vs { pokemonB[ 'name' ] } fue: { datosBatallas[ f"{ pokemonA[ 'name' ] }-{ pokemonB[ 'name' ] }" ][ 0 ].upper() }" )
        return Battle_Result( registro_existente = True, ganador_nombre = datosBatallas[ f"{ pokemonA[ 'name' ] }-{ pokemonB[ 'name' ] }" ][ 0 ].upper(), perdedor_nombre = datosBatallas[ f"{ pokemonA[ 'name' ] }-{ pokemonB[ 'name' ] }" ][ 2 ].upper(), iniciador_nombre = datosBatallas[ f"{ pokemonA[ 'name' ] }-{ pokemonB[ 'name' ] }" ][ 1 ].upper() )
    logger.info( "------------- BATALLA POKEMON -------------\n")
    logger.info( f"---=====[ { pokemonA[ 'name' ].upper() } VS { pokemonB[ 'name' ].upper() } ]=====---\n" )
    logger.info( "-" * 43 )
    ganador, iniciador, perdedor = pelear( pokemonA, pokemonB )
    datosBatallas[ f"{ pokemonA[ 'name' ] }-{ pokemonB[ 'name' ] }" ] = ganador, iniciador, perdedor
    datosBatallas[ f"{ pokemonB[ 'name' ] }-{ pokemonA[ 'name' ] }" ] = ganador, iniciador, perdedor
    guardar( datosBatallas )
    return Battle_Result( registro_existente = False, ganador_nombre = datosBatallas[ f"{ pokemonA[ 'name' ] }-{ pokemonB[ 'name' ] }" ][ 0 ].upper(), perdedor_nombre = datosBatallas[ f"{ pokemonA[ 'name' ] }-{ pokemonB[ 'name' ] }" ][ 2 ].upper(), iniciador_nombre = datosBatallas[ f"{ pokemonA[ 'name' ] }-{ pokemonB[ 'name' ] }" ][ 1 ].upper() )