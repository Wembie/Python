def menuLineas():
    print( """1 -> Linea Uno.
2 -> Linea Dos
3 -> Linea Tres
4 -> Linea Cuatro""")

def lineaMasGanada( vecesLinea1, vecesLinea2, vecesLinea3, vecesLinea4 ):
    if vecesLinea1 < vecesLinea4 and vecesLinea2 < vecesLinea4 and vecesLinea3 < vecesLinea4:
        return 4
    elif vecesLinea1 < vecesLinea3 and vecesLinea2 < vecesLinea3 and vecesLinea4 < vecesLinea3:
        return 3
    elif vecesLinea1 < vecesLinea2 and vecesLinea3 < vecesLinea2 and vecesLinea4 < vecesLinea2:
        return 2
    elif vecesLinea2 < vecesLinea1 and vecesLinea3 < vecesLinea1 and vecesLinea4 < vecesLinea1:
        return 1
    else:
        return 0
def lineaMenosGanada( vecesLinea1, vecesLinea2, vecesLinea3, vecesLinea4 ):
    if vecesLinea1 > vecesLinea4 and vecesLinea2 > vecesLinea4 and vecesLinea3 > vecesLinea4:
        return 4
    elif vecesLinea1 > vecesLinea3 and vecesLinea2 > vecesLinea3 and vecesLinea4 > vecesLinea3:
        return 3
    elif vecesLinea1 > vecesLinea2 and vecesLinea3 > vecesLinea2 and vecesLinea4 > vecesLinea2:
        return 2
    elif vecesLinea2 > vecesLinea1 and vecesLinea3 > vecesLinea1 and vecesLinea4 > vecesLinea1:
        return 1
    else:
        return 0

def resultados( totalDineroLineas, usuariosTotales, cantidadApuestas, lineaMasGanadora, lineaMenosGanadora  ):
    print( f"""Linea mas Ganadora = Linea { lineaMasGanadora }
Linea menos Ganadora = Linea { lineaMenosGanadora }
Dinero recaudado = { totalDineroLineas }
Promedio dinero apuesta = { totalDineroLineas / cantidadApuestas }
Cantidad usuarios totales = { usuariosTotales }""")

def main():
    horaAbierta = 9
    horaCerrada = 17
    mediaHora = 0.5
    dineroLinea1 = 0
    dineroLinea2 = 0
    dineroLinea3 = 0
    dineroLinea4 = 0
    vecesLinea1 = 0
    vecesLinea2 = 0
    vecesLinea3 = 0
    vecesLinea4 = 0
    usuariosTotales = 0
    cantidadApuestas = 0
    print( "-> Hipodromo <- \n-> by: Daniel Palacios <-\n" )
    while horaAbierta < horaCerrada:
        print( horaAbierta )
        cantidadApuestas += 1
        print( f"Apuesta Numero: { cantidadApuestas }" )
        lineasHipodromo = 4
        menuLineas()
        lineaGanadora = int( input( "Digita la linea ganadora: " ) )
        if lineaGanadora == 1:
            vecesLinea1 += 1
        elif lineaGanadora == 2:
            vecesLinea2 += 1
        elif lineaGanadora == 3:
            vecesLinea3 += 1
        elif lineaGanadora == 4:
            vecesLinea4 += 1
        for linea in range( lineasHipodromo ):
            cuantosUsuarios = int( input( f"Digita la cantidad de ususarios de la linea { linea + 1 }: " ) )
            usuariosTotales += cuantosUsuarios
            for usuario in range( cuantosUsuarios ):
                dineroUsuario = float( input( f"Digita el dinero apostado del usuario { usuario + 1 } en la linea { linea + 1 }: " ) )
                if linea == 0:
                    dineroLinea1 += dineroUsuario
                elif linea == 1:
                    dineroLinea2 += dineroUsuario
                elif linea == 2:
                    dineroLinea3 += dineroUsuario
                elif linea == 3:
                    dineroLinea4 += dineroUsuario
        print( "" )
        horaAbierta += mediaHora
    totalDineroLineas = dineroLinea1 + dineroLinea2 + dineroLinea3 + dineroLinea4
    lineaMasGanadora = lineaMasGanada( vecesLinea1, vecesLinea2, vecesLinea3, vecesLinea4 )
    lineaMenosGanadora = lineaMenosGanada( vecesLinea1, vecesLinea2, vecesLinea3, vecesLinea4 )
    if lineaMasGanadora == 0:
        lineaMasGanadora = "Son Iguales"
    if lineaMenosGanadora == 0:
        lineaMenosGanadora = "Son Iguales"
    resultados( totalDineroLineas, usuariosTotales, cantidadApuestas, lineaMasGanadora, lineaMenosGanadora )
main()