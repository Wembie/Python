import random
from collections import deque
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import scrolledtext as st

#Cache Completamente Asociativa, con política de reemplazo FIFO y política de actualización write back.

CAPACIDAD_DIRECCIONAMIENTO_SISTEMA = 2048
TOTAL_BLOQUES = 32

def abrirArchivo():
    global archivo, almacenamientoRam
    archivo = filedialog.askopenfilename( title = "Abrir Archivo", initialdir = "C:/", filetypes = ( ( "Archivo de Texto", ".txt" ) ,( "Todos los Archivos", ".*" ) ) )
    almacenamientoRam = []
    if archivo != "":
        ram.delete( "1.0", END )
        file = open( archivo, "r", encoding = "utf-8" )
        for i in range( CAPACIDAD_DIRECCIONAMIENTO_SISTEMA ):
            contenido = file.readline().strip()
            almacenamientoRam.append( contenido )
            ram.insert( INSERT, contenido + "\n" )
        file.close() 
    else:
        ram.delete( "1.0", END )

def generarDatosRamAleatorios():
    global almacenamientoRam
    almacenamientoRam = []
    ram.delete( "1.0", END )
    for i in range( CAPACIDAD_DIRECCIONAMIENTO_SISTEMA ):
        contenido = ""
        for j in range( 8 ):
            contenido += str( random.randint( 0, 1 ) )
        almacenamientoRam.append( contenido )
        ram.insert( INSERT, contenido + "\n" )

def verificarArchivo():
    try:
        try:
            open( archivo, 'r' )
            return True
        except NameError:
            return False
    except IOError:
        return False

def sumarHits():
    if verificarArchivo() or len( almacenamientoRam ) > 0:
        if veces.get() > 0:
            ramMofidicada.delete( "1.0", END ) 
            cache.delete( "1.0", END ) 
            hits = 0
            almacenamientoCache = deque()
            for i in range( TOTAL_BLOQUES ):
                #Dirty | Bit Validacion | Tag | Data
                #  0   |        1       |  2  |  3
                almacenamientoCache.append( [ "0", "0", None, None ] )
            for i in range( veces.get() ):
                tag = ""
                index = ""
                offset = ""
                for j in range( 3 ):
                    tag += str( random.randint( 0, 1 ) )
                    offset += str( random.randint( 0, 1 ) )
                for j in range( 5 ):
                    index += str( random.randint( 0, 1 ) )
                
                address = tag + index + offset
                leerOEscribir = random.randint( 0, 1 )
                print(address, leerOEscribir)
                hiteo = False
                tag += index
                for j in range( TOTAL_BLOQUES ):
                    if almacenamientoCache[ j ][ 2 ] == tag:
                        hits += 1
                        hiteo = True
                        if leerOEscribir == 1: #Escribiendo
                            contenido = ""
                            for k in range( 8 ):
                                for l in range( 8 ):
                                    contenido += str( random.randint( 0, 1 ) )
                                contenido += " "
                            almacenamientoCache[ j ][ 3 ] = contenido
                            almacenamientoCache[ j ][ 0 ] = "1"
                            almacenamientoCache[ j ][ 1 ] = "1"
                        break
                #Reemplaza Cache
                if hiteo == False:
                    primeraPosDatos = int( tag + "000", 2 )
                    ultimaPosDatos = int( tag + "111", 2 ) + 1
                    datosRam = ""
                    for j in range( primeraPosDatos, ultimaPosDatos ):
                        datosRam += almacenamientoRam[ j ] + " "
                    #FIFO
                    writeBack = almacenamientoCache.popleft()
                    if writeBack[ 0 ] == "1":
                        if leerOEscribir == 1: #Escribiendo
                            datosRam = ""
                            for k in range( 8 ):
                                for l in range( 8 ):
                                    datosRam += str( random.randint( 0, 1 ) )
                                datosRam += " "
                        else:
                            posicion = 0
                            for j in range( primeraPosDatos, ultimaPosDatos ):
                                almacenamientoRam[ j ] = writeBack[ 3 ].split()[ posicion ] #+ " CAMBIADO"
                                posicion += 1      
                    almacenamientoCache.append( [ "1", "1", tag, datosRam ] )
            for i in range( len( almacenamientoRam ) ):
                ramMofidicada.insert( INSERT, almacenamientoRam[ i ] + "\n" )
            for i in range( len( almacenamientoCache ) ):
                for j in range( len( almacenamientoCache[ i ] ) ):
                    if almacenamientoCache[ i ][ j ] is None:
                        cache.insert( INSERT, "None " )
                    else:
                        cache.insert( INSERT, almacenamientoCache[ i ][ j ] + " " )
                cache.insert( INSERT, "\n" )
                    
            messagebox.showinfo( title = "Info", message = f"Tasa de aciertos (HITS): { hits }" )
        else:
            messagebox.showwarning( title = "Alerta", message = "Recuerda colocar las veces a realiazar la simmulacion" )
    else:
        messagebox.showerror( title = "Error", message = "No has seleccionado ningun archivo" )

def main():
    #Iniciacion interfaz
    global programa, ram, ramMofidicada, cache, validar, veces
    programa = Tk()
    programa.title( "Cache" )
    programa.geometry( '1400x320' )
    #programa.iconbitmap( "binario.ico" )
    programa.configure( background = 'light sea green' )
    #Textos
    Label( programa, text = "Juan Acosta", background = 'light sea green' ).place( x = 300, y = 0 )
    Label( programa, text = "Datos en Ram", background = 'light sea green' ).place( x = 100, y = 290 )
    Label( programa, text = "Datos en Ram Modificados", background = 'light sea green' ).place( x = 455, y = 290 )
    Label( programa, text = "Cache", background = 'light sea green' ).place( x = 1000, y = 290 )
    Label( programa, text = "Veces", background = 'light sea green' ).place( x = 314, y = 60 )
    ram = st.ScrolledText( programa, width = 30, height = 16 )
    ram.grid( column = 0, row = 0, padx = 10, pady = 30 )
    ramMofidicada = st.ScrolledText( programa, width = 32, height = 16 )
    ramMofidicada.grid( column = 2, row = 0, padx = 10, pady = 30 )  
    cache = st.ScrolledText( programa, width = 86, height = 16 )
    cache.grid( column = 3, row = 0, padx = 0, pady = 30 )
    #Entradas
    veces = IntVar()
    Entry( programa, textvariable = veces, width = 10 ).place( x = 300, y = 80 )
    #Botones
    Button( programa, text = "Aleatorio", command = generarDatosRamAleatorios ).place( x = 302, y = 110 )
    Button( programa, text = "Abrir Archivo", command = abrirArchivo ).grid( column = 1, row = 0, padx = 10, pady = 20 ) 
    Button( programa, text = "Simular", command = sumarHits ).place( x = 304, y = 185 )
    #Ciclo
    programa.mainloop()

main()