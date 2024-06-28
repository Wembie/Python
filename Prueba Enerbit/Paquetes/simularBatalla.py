from Paquetes.datos import cargar, guardar
from Paquetes.preguntarPokemon import preguntar
from Paquetes.peleaPokemon import pelear

datosBatallas = cargar()   

def simular():
    pokemonA = preguntar( "1" )
    pokemonB = preguntar( "2" )
    if pokemonA[ 'name' ] == pokemonB[ 'name' ]:
        pokemonA[ 'name' ] += "1"
        pokemonB[ 'name' ] += "2"
    if f"{ pokemonA[ 'name' ] }-{ pokemonB[ 'name' ] }" in datosBatallas or f"{ pokemonB[ 'name' ] }-{ pokemonA[ 'name' ] }" in datosBatallas:
        print( "La batalla ya se encontraba en nuestros registros..." )
        if pokemonA[ 'speed' ] == pokemonB[ 'speed' ]:
            print( f"ACLARANDO COMO TIENEN LA MISMA VELOCIDAD EN ESTA OCASION EL INICIADOR FUE: { datosBatallas[ f"{ pokemonA[ 'name' ] }-{ pokemonB[ 'name' ] }" ][ 1 ].upper() } ")
        print( f"El ganador de la batalla pokemon de { pokemonA[ 'name' ] } vs { pokemonB[ 'name' ] } fue: { datosBatallas[ f"{ pokemonA[ 'name' ] }-{ pokemonB[ 'name' ] }" ][ 0 ].upper() }" )
        return
    print( "------------- BATALLA POKEMON -------------\n")
    print( f"---=====[ { pokemonA[ 'name' ].upper() } VS { pokemonB[ 'name' ].upper() } ]=====---\n" )
    print( "-" * 43 )
    ganador, iniciador = pelear( pokemonA, pokemonB )
    datosBatallas[ f"{ pokemonA[ 'name' ] }-{ pokemonB[ 'name' ] }" ] = ganador, iniciador
    datosBatallas[ f"{ pokemonB[ 'name' ] }-{ pokemonA[ 'name' ] }" ] = ganador, iniciador
    guardar( datosBatallas )