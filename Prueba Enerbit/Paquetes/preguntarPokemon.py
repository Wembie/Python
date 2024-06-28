from Paquetes.extraerPokemon import extraer

def preguntar( numero ):
    verificar = True
    while verificar:
        nombrePokemon = input( f"Digita el nombre del Pokemon #{ numero }: " )
        verificar, pokemon = extraer( nombrePokemon )
    return pokemon