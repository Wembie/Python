from sys import stdin

def main():
    texto1 = []
    texto2 = []
    file = open( "texto1.txt", "r", encoding = "utf-8" )
    for i in range( 2048 ):
        texto1.append( file.readline().strip() )
    file.close()
    file = open( "texto2.txt", "r", encoding = "utf-8" )
    for i in range( 2048 ):
        texto2.append( file.readline().strip() )
    file.close()
    file = open("generado.txt", "w", encoding = "utf-8")
    for i in range( 2048 ):
        if texto1[ i ] != texto2[ i ]:
            file.write( f"Index: { i } Texto1: { texto1[ i ] } -> Texto2: { texto2[ i ] } \n" )
    file.close()
main()