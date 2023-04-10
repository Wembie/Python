"""#Operadores Logicos

# AND = and 
# OR = or 
# NOT = not 

numero = 5
numeroDos = 6

if numero > 0 and numeroDos > 0:
    print("hola")

#Ciclos

#While

i = 0
while i < 4:
    i = i + 1
    # i += 1
    print( i )

veces = int(input( "Digita un numero: " ) )
suma = 0
i = 0
while i < veces:
    suma += i #0+0 = 0, 0+1 = 1, 1+2 = 3, 3+3 = 6, 6+4 = 10
    print( suma )
    i += 1
#print( "La suma total es:", suma )
print( f"La suma total es: {suma}" )

#For

for i in range( 11 ):
    print( i )

cadena = "El Parce"
for letra in cadena:
    print( letra )

veces = int(input("¿Cuántas veces quiere que le salude?:  ") ) 
for i in range( veces ):
    print("Hola ", end="")
print("\nAdiós")

lista = [ 1, 2, 3, 4 ]
for i in lista:
    print( i )

for i in range( 3, 10, 2 ): 
    print( i )  #   #  #
                #   #  #De a cuanto va a aumentar
                #   #Final
                #Inicio
#Osea que imprime ("3,5,7,9")

#Funciones

#-> def

#Procedimientos
#Cuando no se retorna nada

def decirHola():
    print( "Hola" )
decirHola()

#Funciones
#Cuando si se retorna algo

def sumarRetornada( valor1, valor2 ):
    return valor1 + valor2
print( sumarRetornada( 4, 5 ) )

def sumarImpresa( valor1, valor2 ):
    print( valor1 + valor2 )
sumarImpresa( 4, 5 )

def primo( valor ):
    if valor < 1 :
        return False
    elif valor == 2 :
        return True
    else:
        for i in range( 2, valor ):
            if valor % i == 0:
                return False
        return True
esPrimo = primo( 11 )
if esPrimo is True :
    print ( "Es Primo" )
else:
    print ( "No es Primo" )

#Banderas 

import random 

bandera = 0
#numeroMagico = random.randint( 1, 3 )
while True:
    numeroMagico = random.randint( 1, 3 )
    numero = int(input( "Digite un numero [0, 1, 2, 3]: " ) )
    if numero == 0:
        #Hasta que digite 0, rompe
        break
    if numero == numeroMagico and bandera == 0:
        print( "Uno" )
        bandera = 1
    elif numero == numeroMagico and bandera == 1:
        print( "Uno x2" )
        bandera = 2
    elif numero == numeroMagico and bandera == 2:
        print( "Uno x3" )

#Ejercicio resulto del taller del parce
def contarCaracteresCadena( cadena ):
    contadorCaracteres = 0
    for letra in cadena:
        contadorCaracteres += 1
    return contadorCaracteres
cadena = "Chupapimuyaño"
print(f"La cadena { cadena } tiene { contarCaracteresCadena( cadena ) } caracteres" )
cadena = "Parce"
print(f"La cadena { cadena } tiene { contarCaracteresCadena( cadena ) } caracteres" )
cadena = "Ou dari, ahhhhhh, Chupapimuyaño, ohh that cream, lechita papi"
print(f"La cadena { cadena } tiene { contarCaracteresCadena( cadena ) } caracteres" )

#1) Elabore una función que reciba por parámetro una cadena y retorne como resultado cuántas vocales (mayúsculas o minúsculas) tenía la cadena en total

def contarVocalesMinMay( cadena ):
    vocalesMinusculas = [ "a", "e", "i", "o", "u" ] 
    vocalesMayusculas = [ "A", "E", "I", "O", "U" ]
    contadorVocales = 0
    for letra in cadena:
        if letra in vocalesMinusculas or letra in vocalesMayusculas:
            contadorVocales += 1
    return contadorVocales
cadena = "ChUpaPiMuYaÑo"
print( f"La cadena { cadena } tiene { contarVocalesMinMay( cadena ) } vocales ( Minusculas o Mayusculas )" )

#Listas
#EMPIEZAN EN 0 y la ultima posision es -1

nombre.append( x ) #Adiciona x elemento a la lista 
nombre.clear() #Borra todos los elementos de la lista
nombre.copy() #retorna una copia de la lista
nombre.count( e ) #retorna el numero de elementos existentes en la lista que son iguales al elemento (e)
nombre.index( e ) #retorna el indice del primer elemento que sea igual al elemento (e)
nombre.insert( p, e ) #inserta un elemento (e) en la posicion (p) de la lista
nombre.pop(p) #Borra el elemento que este en la posicion (p)
nombre.extend( e, e, e, e ) #etc Adiciona varios elementos a la vez donde (e) puede ser cualquiera
#nombre.sort() #Ordena la lista
nombre.sort() #Ordena la lista de manor a mayor
nombre.sort( reverse = True ) #Ordena de mayor a menor

nombre = [ "Nuby" ]
print( nombre )
nombre.append( "Parce" )
nombre.append( True )
nombre.append( 69 )
print( nombre )

#Recorrer una lista

for elemento in nombre:
    print( elemento )

for indice in range( len( nombre ) ):
    print( f"Indice = { indice }" )
    print( f"Elemento = { nombre[ indice ] }" )
#Dada una lista de numeros, cree una funcion para returnar la suma de ellos

#len( lista ) -> retorna el size de la lista

def sumarElementosLista( lista ):
    sumaLista = 0
    for i in range( len( lista ) ):
        sumaLista += lista[ i ]
        #lista [ 0 ] = 1
        #lista [ 1 ] = 2
        #lista [ 2 ] = 3
        #lista [ 3 ] = 4
        #lista [ 4 ] = 5
    return sumaLista
listaNumeros = [ 1, 2, 3, 4, 5 ]
print( f"La suma de la lista { listaNumeros } es de: { sumarElementosLista( listaNumeros ) }" )

#1) Cree una función que le pregunte al usuario cuantos números desea que tenga una 
# lista (por ejemplo 50), y con base en ese número, llene una lista por medio de números 
# aleatorios (utilizando randint(0,101)) de manera que cada número aleatorio será cada 
# valor de su lista. Como resultado usted debe retornar la lista llena de números.   

import random

def crearListaAleatoria():
    lista = []
    tamaño = int( input( "Digite de cuantos numeros desea la lista aleatoria: ") )
    for i in range( tamaño ):
        lista.append( random.randint( 0, 101 ) )
    return lista
print( crearListaAleatoria() )

#3) Realice un programa que, dada una lista, retorne otra lista con los valores
#  invertidos: Ejemplo, si la lista es [2,3,4], retorna [4,3,2]

lista = [ 2, 3, 4]

def invertirListaConHack( lista ):
    return lista[ ::-1 ]

print( invertirListaConHack( lista ) )

def invertirListaSinHack( lista ):
    listainvertida = []
    for i in range( len( lista ) - 1, - 1, - 1 ): #voy desde el ultimo elemento de la lista-1, hasta el primer elemento de la lista-1, y va disminuir de a -1
        listainvertida.append( lista[ i ] )
    return listainvertida

print( invertirListaSinHack( lista ) )

#9) Realice una función que recibe como parámetro dos listas. 
# La primera lista LE contiene los elementos a reorganizar, 
# la segunda lista LP contiene las nuevas posiciones de los elementos de 
# la lista LE. La función con los parámetros: LE = [”a”, ”b”, ”c”, ”d”] 
# LP = [1, 3, 0, 2] debería retornar la lista [”c”, ”a”, ”d”, ”b”].

def cambiarPosicionesLista( lista1, lista2 ):
    listaLE = []
    for i in range( len( lista1 ) ):
        listaLE.insert( lista2[ i ], lista1[ i ] )
    return listaLE   
listaLE = [ "a", "b", "c", "d" ]
listaLP = [ 1, 3, 0, 2 ]
print( cambiarPosicionesLista( listaLE, listaLP ) )

#10 Realice un programa que basado en 2 listas, construya la intersección de conjuntos
#  de ellas (los elementos que están en la lista A y los elementos que están en la lista
#  B) en una tercera lista, la nueva lista NO PUEDE tener elementos repetidos.

import random

def interseccion( lista1, lista2 ):
    listaInterseccionada = []
    for i in lista1:
        for j in lista2:
            if i == j:
                if i not in listaInterseccionada:
                    listaInterseccionada.append( i )
    return listaInterseccionada
numerosNaturales = []
numerosAleatorios = []
for i in range( 10 ):
    numerosNaturales.append( random.randint( 0, 8 ) )
    numerosAleatorios.append( random.randint( 0, 8 ) )
print( numerosNaturales, numerosAleatorios )
print( interseccion( numerosNaturales, numerosAleatorios ) )

#Matrices

matriz = [ [ 1, 2 ], [ 3, 4 ] ]
#filas = len( matriz )
#columna = len( matriz[ i ] )
#print( matriz[ 0 ][ 0 ] ) #Imprime 1

#Recorrer Matriz

for i in matriz:
    #print( i )
    for j in i:
        print( j )

for i in range( len( matriz ) ):
    #print( matriz[ i ] )
    for j in range( len( matriz[ i ] ) ):
        print( matriz[ i ][ j ] )

def pares( matriz ):
    lista = []
    for i in range( len( matriz ) ):
        for j in range( len( matriz[ i ] ) ):
            if matriz[ i ][ j ] % 2 == 0:
                lista.append( matriz[ i ][ j ] )
    return lista
matriz = [ [ 1, 2 ], [ 3, 4 ], [ 5, 6 ] ]
print( pares( matriz ) )

#Dada una matriz contar cuantos números positivos, negativos o ceros tiene
#retornandolos en una matriz con los 3 elementos pedidos y en cada columna
#deberia dar el nombre y cuantos, es decir [["Positivos", 8], ["Negativos", 6],["Neutros", 3]]

def contarPN0( matriz ):
    contadorPositivos = 0
    contadorNegativos = 0
    contadorNeutros = 0
    for i in range( len( matriz ) ):
        for j in range( len( matriz[ i ] ) ):
            if matriz[ i ][ j ] > 0:
                contadorPositivos += 1
            elif matriz[ i ][ j ] < 0:
                contadorNegativos += 1
            else:
                contadorNeutros += 1
    matrizARetornar = []
    listaPositivos = [ "Positivos" ]
    listaPositivos.append( contadorPositivos )
    listaNegativos = [ "Negativos" ]
    listaNegativos.append( contadorNegativos )
    listaNeutros = [ "Neutros" ]
    listaNeutros.append( contadorNeutros )
    matrizARetornar.append( listaPositivos )
    matrizARetornar.append( listaNegativos )
    matrizARetornar.append( listaNeutros )
    return matrizARetornar
matriz = [ [ -4, 1, 0, 3 ], [ 4, 3, 1, 0 ], [ -5, -3, 0, 1 ] ]
print( contarPN0( matriz ) )

#1) Una matriz es espejo de otra, cuando los elementos de cada posición de
#  la primera matriz son exactamente iguales a los elementos de cada posición
#  de la segunda matriz. Realice una función que recibe 2 matrices por parámetro
#  y responde verdadero si son espejo o falso si no lo son. Debe validar que las
#  2 matrices sean del mismo tamaño.

def espejoSinHack( matriz1, matriz2 ):
    if len( matriz1 ) == len( matriz2 ) and len( matriz1[ 0 ] ) == len( matriz2[ 0 ] ):
        for i in range( len( matriz1 ) ):
            for j in range( len( matriz1[ i ] ) ):
                if matriz1[ i ][ j ] != matriz2[ i ][ j ]:
                    return False
        return True
    else:
        return False
def espejoConHack( matriz1, matriz2 ):
    if matriz1 == matriz2:
        return True
    else:
        return False
matrizA = [ [ 1, 3, 5, 6 ], [ 4, 6, 8, 1 ] ]
matrizB = [ [ 1, 3, 5], [ 4, 6, 8, 1 ] ]
matrizC = [ [ 1, 3, 5, 6 ], [ 4, 6, 8, 1 ] ]
print( "Sin Hack: " )
print( espejoSinHack( matrizA, matrizB ) )
print( espejoSinHack( matrizB, matrizC ) )
print( espejoSinHack( matrizA, matrizC ) )
print( "Con Hack: " )
print( espejoConHack( matrizA, matrizB ) )
print( espejoConHack( matrizB, matrizC ) )
print( espejoConHack( matrizA, matrizC ) )

#Dada una matriz, cree una funcion que retorna otra lista 
# con los numeros repetidos de dicha matriz y verificar que no se repitan

def darRepetidos( matriz ):
    listaRepetidos = []
    for i in range( len( matriz ) ):
        for j in range( len( matriz[ i ] ) ):
            listaRepetidos.append( matriz[ i ][ j ] )
    listaRepetidosUnicos = []
    listaRepetidosRepetidos = []
    for i in range( len( listaRepetidos ) ):
        if not listaRepetidos[ i ] in listaRepetidosUnicos:
            listaRepetidosUnicos.append( listaRepetidos[ i ] )
        else:
            if not listaRepetidos[ i ] in listaRepetidosRepetidos:
                listaRepetidosRepetidos.append( listaRepetidos[ i ] )
    return listaRepetidosRepetidos, listaRepetidosUnicos
matrizNumeros = [ [ 1, 3, 5, 6 ], [ 4, 6, 8, 1 ], [ 3, 6, 3, 7, 1, 9, 5 ] ]
#1 3 5 6 
#NO
# 4 8 7 9
[ repetidos, lista ] = darRepetidos( matrizNumeros )
print( f"Repetidos: { repetidos } \nLista: { lista }" )

#Diccionarios

name = {}
name = dict() #Lo mismo

name = { "Parce": "EL PARCEEEEEEEEE" }
print( name )
print( name[ "Parce" ] )

numeros = { "Num": [ 1, 2, 3, 4, 5] }
print( numeros[ "Num" ] )
print( numeros[ "Num" ][ 4 ] )
numeros[ "Num" ].append( "Parce" )
print( numeros[ "Num" ] )

#SABER LLAVES
diccionario = { "Nota1":5, 2:"Nota2", "Nota3":4, 20.20:True }
for key in diccionario:
    print( f"La llave es: { key } y su valor es: { diccionario[ key ] }" )

nombre = dict( Nombre = "Uber", Apellido = "Puta", Años = 69 )
print( nombre )
print( nombre[ "Nombre" ] )

diccionario = { 'a': 1, 'b': 2, 'c': 3, 'd': 4 }
llaves = diccionario.keys()
items = diccionario.items()
valores = diccionario.values()
print( llaves )
print( items )
print( valores )
diccionario.pop( 'b' )
print( diccionario )
#Saber lo q hay en la llave
valor = diccionario.get( 'd' )
print( valor )
diccionario.clear()
print( diccionario )

#Realize un programa que dado un diccionario le pregunte la fruta que desee, los kilos y si la fruta
#que digita no esta en el diccioinario hagaselo saber y los valores de la fruta los multiplica por
#los kilos q desea llevar y hagaselo saber cuanto cuestan

dic = { 'Banano': 600, 'Mango': 1000, 'Pera': 700, 'Manzana': 300 }
fruta = input( "Digite la fruta que desea: " )
kilos = int( input( "Digite la cantidad de kilos: " ) )
if fruta in dic:
    print( f"{ kilos } kilos de { fruta } cuestan: { dic[ fruta ] * kilos }" )
else:
    print( "La fruta no se encuentra" )"""

#Dado un diccionario de codigos morse, pidale al usuario una palabra y se la devuelve en morse
morse = {
    'A': '.-',     'B': '-...',    'C': '-.-.',
    'D': '-..',    'E': '.',       'F': '..-.',
    'G': '--.',    'H': '....',    'I': '..',
    'J': '.---',   'K': '-.-',     'L': '.-..',
    'M': '--',     'N': '-.',      'O': '---',
    'P': '.--.',   'Q': '--.-',    'R': '.-.',
    'S': '...',    'T': '-',       'U': '..-',
    'V': '...-',   'W': '.--',     'X': '-..-',
    'Y': '-.--',   'Z': '--..',    '1': '.----',
    '2': '..---',  '3': '...--',   '4': '....-',
    '5': '.....',  '6': '-....',   '7': '--...',
    '8': '---..',  '9': '----.',   '0': '-----',
    '.': '.-.-.-', ',': '--..--',  ':': '---...',
    ';': '-.-.-.', '?': '..--..',  '!': '-.-.--',
    '"': '.-..-.', "'": '.----.',  '+': '.-.-.',
    '-': '-....-', '/': '-..-.',   '=': '-...-',
    '_': '..--.-', '$': '...-..-', '@': '.--.-.',
    '&': '.-...',  '(': '-.--.',   ')': '-.--.-',
    ' ': ' '
}
print( morse.items() )
palabra = input( "Digite la Palabra deseada: " )
palabra = palabra.upper()
resultado = ""
for i in palabra:
    resultado += morse[ i ]
print( resultado )
