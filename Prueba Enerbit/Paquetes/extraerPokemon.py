import requests

url = 'https://pokeapi.co/api/v2/pokemon/'

def extraer( nombrePokemon ):
    respuesta = requests.get( url + nombrePokemon.lower() )
    if respuesta.status_code == 200:
        datosPokemon = respuesta.json()
        return False, {
            'name': datosPokemon[ 'name' ],
        **{ stat[ 'stat' ][ 'name' ] : stat[ 'base_stat' ] for stat in datosPokemon[ 'stats' ] }
    } 
    #return respuesta.status_code
    print( f"No se ha encontrado el Pokemon { nombrePokemon }, intenta con otro." )
    return True, None