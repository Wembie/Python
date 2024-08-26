from Service.funtions import imprimirStats, logger

import random

def pelear( pokemonA, pokemonB ):
    if pokemonA[ 'speed' ] > pokemonB[ 'speed' ]:
        iniciador = pokemonA
        sucesor = pokemonB
    elif pokemonB[ 'speed' ] > pokemonA[ 'speed' ]:
        iniciador = pokemonB
        sucesor = pokemonA
    else: #Empate
        elegido = random.choice( [ pokemonA[ 'name' ], pokemonB[ 'name' ] ] )
        if elegido == pokemonA[ 'name' ]:
            iniciador = pokemonA
            sucesor = pokemonB
        else:
            iniciador = pokemonB
            sucesor = pokemonA
    reduccionDefensaA = 1
    reduccionDefensaB = 1
    logger.info( f"INICIADOR: { iniciador[ 'name' ].upper() }\n\nSTATS\n" ) 
    imprimirStats( iniciador )
    logger.info( f"\nSUCESOR: { sucesor[ 'name' ].upper() }\n\nSTATS\n" )
    imprimirStats( sucesor )
    logger.info( F"\nEMPIEZAAAAAAAAAAAAAAAAA LA BATALAAAAAAAAAAAAA { iniciador[ 'name' ].upper() } HACE SU PRIMER ATAQUE BASICO!")
    while iniciador[ 'hp' ] > 0 and sucesor[ 'hp' ] > 0:
        logger.info( f"\nTURNO DE { iniciador[ 'name' ].upper() }")
        if reduccionDefensaB % 2 == 0:
            defensaActual = sucesor[ 'defense' ]
            sucesor[ 'defense' ] -= sucesor[ 'defense' ] * 0.2
            logger.info( f"{ iniciador[ 'name' ] } ha roto la defensa de { sucesor[ 'name' ] } en un 20%" )
            logger.info( f"Defensa Antes: { defensaActual }, Defensa Ahora: { sucesor[ 'defense' ] } ")
        ataque = max( 0, iniciador[ 'attack' ] - sucesor[ 'defense' ] )
        sucesor[ 'hp' ] -= ataque
        if ataque:
            logger.info( f"ATAQUE ACERTADO!!!!, { iniciador[ 'name' ] } logra hacer un daño de { ataque } a { sucesor[ 'name' ] }" )
            if sucesor[ 'hp' ] <= 0:
                logger.info( f"\n{ sucesor[ 'name' ] } ha sido derrotado. { iniciador[ 'name' ] } es el ganador!, FELICIDADES!!!!!!" )
                return iniciador[ 'name' ], iniciador[ 'name' ], sucesor[ 'name' ]
        else:
            logger.info( f"Lastimosamente el ataque de { iniciador[ 'name' ] } no fue lo suficiente fuerte como para superar la defensa de { sucesor[ 'name' ] }." )
            reduccionDefensaB += 1
        logger.info( f"\nTURNO DE { sucesor[ 'name' ].upper() }")
        if reduccionDefensaA % 2 == 0:
            defensaActual = iniciador[ 'defense' ]
            iniciador[ 'defense' ] -= iniciador[ 'defense' ] * 0.2
            logger.info( f"{ sucesor[ 'name' ] } ha roto la defensa de { iniciador[ 'name' ] } en un 20%" )
            logger.info( f"Defensa Antes: { defensaActual }, Defensa Ahora: { iniciador[ 'defense' ] } ")
        ataque = max( 0, sucesor[ 'attack' ] - iniciador[ 'defense' ] )
        iniciador[ 'hp' ] -= ataque
        if ataque:
            logger.info( f"ATAQUE ACERTADO!!!!, { sucesor[ 'name' ] } logra hacer un daño de { ataque } a { iniciador[ 'name' ] }" )
            if iniciador[ 'hp' ] <= 0:
                logger.info( f"\n{ iniciador[ 'name' ] } ha sido derrotado. { sucesor[ 'name' ] } es el ganador!, FELICIDADES!!!!!!" )
                return sucesor[ 'name' ], iniciador[ 'name' ], iniciador[ 'name' ]
        else:
            logger.info( f"Lastimosamente el ataque de { sucesor[ 'name' ] } no fue lo suficiente fuerte como para superar la defensa de { iniciador[ 'name' ] }." )
            reduccionDefensaA += 1