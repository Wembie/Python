import random

APUESTA = 50000
VECES = 10

GANO = 0
PERDIO = 1

def main():
    ganancia = 0
    ganadasPerdidas = [ 0, 0 ]
    maximo = 0
    minimo = 0
    apuesta = APUESTA
    for _ in range( VECES ):
        numeroRuleta = random.randint( 0, 36 )
        if numeroRuleta >= 4 and numeroRuleta <= 33:
            ganancia += apuesta
            apuesta = APUESTA
            ganadasPerdidas[ GANO ] += 1
            maximo = max( maximo, ganancia )
        else:
            ganancia -= ( apuesta * 5 )
            ganadasPerdidas[ PERDIO ] += 1
            minimo = min( minimo, ganancia )
            #apuesta *= 2
            print(apuesta)    
    print( f"Gane: { ganadasPerdidas[ GANO ] } veces\nPerdi: { ganadasPerdidas[ PERDIO ] } veces\nMaxima Perdida: { minimo }\nMaximo Ganancia: { maximo }\nLo que aposte: { apuesta * VECES }\nComo me fue: { ganancia }\nCon lo que sali: { ( apuesta * VECES ) + ganancia }" )
    
main()