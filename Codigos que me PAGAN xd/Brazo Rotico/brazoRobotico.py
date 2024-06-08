def menu( combustible ):
    while True:
        print( f"""-> Menu Brazo Robotico <-\n
D -> Desplazar a la derecha.
I -> Desplazar a la izquierda.
S -> Terminar Ejecucion.\n
Combustible restante: { combustible }.\n""" )
        opcion = input( "Digita la opcion: " )
        if opcion.upper() == "D" or opcion.upper() == "I" or opcion.upper() == "S":
            print( "" )
            return opcion.upper()
        else:
            print( "\nOpcion invalida\n" )
posicionBrazo = 0
rangoMayor = 359
combustible = 150
movimientosDerecha = 0
movimientosIzquierda = 0
while combustible > 0:
    opcion = menu( combustible )
    if opcion == "D":
        grados = int( input( "Digita la cantidad de grados: " ) )
        posicionBrazo -= grados
        while posicionBrazo > rangoMayor or posicionBrazo < 0:
            posicionBrazo += rangoMayor
        movimientosDerecha += 1
    elif opcion == "I":
        grados = int( input( "Digita la cantidad de grados: " ) )
        posicionBrazo += grados
        while posicionBrazo > rangoMayor or posicionBrazo < 0:
            posicionBrazo -= rangoMayor
        movimientosIzquierda += 1
    elif opcion == "S":
        break
    print( f"\nPosicion actual del brazo: { posicionBrazo }\n" )
    combustible -= 1
print( f"""Movimientos Derecha: { movimientosDerecha }
Movimientos Izquierda: { movimientosIzquierda }
Movimientos Totales: { movimientosDerecha + movimientosIzquierda }""")