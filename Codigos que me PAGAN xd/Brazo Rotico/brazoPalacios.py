def menu():
    print()
    opcion = input("DIGITE I SI ES IZQUIERDA / D SI ES DERECHA / S SI ES SALIR: ")
    return opcion
def preguntarGrados():
    print()
    grados = int(input("DIGITE LOS GRADOS: "))
    return grados
def mostrarResultados(posBrazo, movIzq, movDer, total, i):
    print("\nPosicion FINAL: ", posBrazo, "°")
    print("Mov Izquierda: ", movIzq)
    print("Mov Derecha: ", movDer)
    print("Total: ", total)
    print("Te sobraron ", i, "de combustible")
def posicionamiento(posBrazo, señal):
    if señal == 0:  #Izquierda
        while posBrazo > 359 or posBrazo < 0:
            posBrazo -= 359
    else: #Derecha
        while posBrazo > 359 or posBrazo < 0:
            posBrazo += 359
    return posBrazo
def main():
    posBrazo = 0 #Se inicia en 0
    movimientos = True
    i = 150 #combustible
    movIzq = 0
    movDer = 0
    total = 0
    while i > 0:
        if i == 75:
            print("Ten cuidado vas por la mitad de combustible")
        mov = menu()
        if mov == "I":
            grados = preguntarGrados()
            posBrazo = posBrazo + grados
            posBrazo = posicionamiento(posBrazo,0)
            movIzq = movIzq + 1
            print("\nPosicion actual: ", posBrazo, "° a la Izquierda")
        elif mov == "D":
            grados = preguntarGrados()
            posBrazo = posBrazo - grados
            posBrazo = posicionamiento(posBrazo,1)
            movDer = movDer + 1
            print("\nPosicion actual: ", posBrazo, "° a la Derecha")
        elif mov == "S":
            total = movIzq + movDer
            mostrarResultados(posBrazo, movIzq, movDer, total, i)
            return
        i = i - 1
    total = movIzq + movDer
    mostrarResultados(posBrazo, movIzq, movDer, total, i)
main()