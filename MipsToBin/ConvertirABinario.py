from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import scrolledtext as st
from diccionario import diccionarioBIN

def abrirArchivo():
    global archivo
    archivo = filedialog.askopenfilename( title = "Abrir Archivo", initialdir = "C:/", filetypes = ( ( "Archivo de Texto", ".txt" ) ,( "Todos los Archivos", ".*" ) ) )
    if archivo != "":
        file = open( archivo, "r", encoding = "utf-8" )
        contenido = file.read()
        file.close()
        texto.delete( "1.0", END ) 
        texto.insert( INSERT, contenido )
    else:
        texto.delete( "1.0", END )


def verificarArchivo():
    try:
        try:
            open( archivo, 'r' )
            return True
        except NameError:
            return False
    except IOError:
        return False

def convertirDecToBin( numero ):
    decimal = bin( numero )
    binario = str( decimal )
    return binario[ 2: ].zfill( 16 )

def convertirHexToBin( numero ):
    hexadecimal = bin( numero )
    binario = str( hexadecimal )
    return binario[ 2: ].zfill( 16 )

def convertirBinToHex( numero ):
    binario = hex( numero )
    return binario[ 2: ]

def convertirABinario():
    if verificarArchivo():
        if frecuencia.get() > 0:
            textoBin.delete( "1.0", END ) 
            diccionarioBinario = diccionarioBIN()
            etiquetas = []
            index = 1
            f = open( archivo, 'r' )
            linea = f.readline()
            while linea != "":
                linea = linea.split()
                if len( linea ) == 1:
                    etiquetas.append( [ linea[ 0 ], index ] )
                else:
                    index += 1
                linea = f.readline()               
            f.close()
            f = open( archivo, 'r' )
            linea = f.readline()
            index = 1
            posicionXDefecto = "0x00400000"
            while linea != "":
                codigoBin = []
                linea = linea.split()
                instrucciones = diccionarioBinario.keys()
                for i in range( len( linea ) ):
                    if linea[ i ] in instrucciones:
                        codigoBin += [ diccionarioBinario[ linea[ i ] ] ]
                    else:
                        if linea[ i ][ 0 ] == "0" and linea[ i ][ 1 ] == "x":
                            codigoBin += [ convertirHexToBin( int( linea[ i ][ 2:6 ], 16 ) ) ]
                        elif linea[ i ][ 0 ].isnumeric():
                            if linea[ i ][ 0 ].isnumeric() and linea[ i ][ 1 ].isnumeric():
                                codigoBin += [ diccionarioBinario[ linea[ i ][ 3:6 ] ] ]
                                codigoBin += [ convertirDecToBin( int( linea[ i ][ 0:2 ] ) ) ]
                            else:
                                codigoBin += [ diccionarioBinario[ linea[ i ][ 2:5 ] ] ]
                                codigoBin += [ convertirDecToBin( int( linea[ i ][ 0 ] ) ) ]
                if linea[ 0 ] == "lui":
                    if linea[ 1 ] in instrucciones and ( linea[ 2 ][ 0 ] == "0" and linea[ 2 ][ 1 ] == "x" ):
                        codigoBinario = codigoBin[ 0 ] + "00000" + codigoBin[ 1 ] + codigoBin[ 2 ]
                        textoBin.insert( INSERT, codigoBinario )
                    else:
                        textoBin.insert( INSERT, f"Error de Sintaxis en { linea[ 0 ] }" )
                elif linea[ 0 ] == "ori" or linea[ 0 ] == "lw" or linea[0] == "sw" or linea[ 0 ] == "sb"or linea[ 0 ] == "sc" or linea[ 0 ] == "sh" or linea[ 0 ] == "addi" or linea[ 0 ] == "addiu" or linea[ 0 ] == "slti" or linea[ 0 ] == "sltiu" or linea[ 0 ] == "andi" or linea[ 0 ] == "lbu" or linea[ 0 ] == "lhu" or linea[ 0 ] == "ll":
                    if linea[ 0 ] == "ori" or linea[ 0 ] == "addi" or linea[ 0 ] == "slti" or linea[ 0 ] == "sltu" or linea[ 0 ] == "andi" or linea[ 0 ] == "addiu":
                        if linea[ 1 ] in instrucciones and linea[ 2 ] in instrucciones and ( linea[ 3 ][ 0 ] == "0" and linea[ 3 ][ 1 ] == "x" ):
                            codigoBinario = codigoBin[ 0 ] + codigoBin[ 2 ] + codigoBin[ 1 ] + codigoBin[ 3 ]
                            textoBin.insert( INSERT, codigoBinario )
                        else:
                            textoBin.insert( INSERT, f"Error de Sintaxis en { linea[ 0 ] }" )
                    else:
                        if linea[ 1 ] in instrucciones and ( ( linea[ 2 ][ 0 ].isnumeric() and linea[ 2 ][ 2:5 ] in instrucciones ) or ( ( linea[ 2 ][ 0 ].isnumeric() and linea[ 2 ][ 1 ].isnumeric() ) and linea[ 2 ][ 3:6 ] in instrucciones ) ):
                            codigoBinario = codigoBin[ 0 ] + codigoBin[ 2 ] + codigoBin[ 1 ] + codigoBin[ 3 ]
                            textoBin.insert( INSERT, codigoBinario )
                        else:
                            textoBin.insert( INSERT, f"Error de Sintaxis en { linea[ 0 ] }" )
                elif linea[ 0 ] =="j" or linea[ 0 ] == "jal":
                    encontroEtiqueta = 0
                    for i in range( len( etiquetas ) ):
                        if linea[ 1 ] == etiquetas[ i ][ 0 ].replace( ":", "" ):
                            encontroEtiqueta = 1
                            break
                    etiqueta = linea[ 1 ]
                    if encontroEtiqueta == 1:
                        for i in range( len( etiquetas ) ):
                            if etiqueta == etiquetas[ i ][ 0 ].replace( ":", "" ):
                                label = ( int( posicionXDefecto[ 2: ] ) + ( ( etiquetas[ i ][ 1 ] - 1 ) * 4 ) ) / 4
                                hexadecimal = bin( int( str( int( label ) ), 16 ) ) 
                                binario = str( hexadecimal )
                                direccion = binario[ 2: ].zfill( 26 ) 
                                codigoBinario = codigoBin[ 0 ] + direccion
                                textoBin.insert( INSERT, codigoBinario )
                    else:
                        textoBin.insert( INSERT, f"Error de Sintaxis en { linea[ 0 ] }" )
                elif linea[ 0 ] == "add" or linea[ 0 ] == "addu" or linea[ 0 ] == "sub" or linea[ 0 ] == "subu" or linea[ 0 ] == "and" or linea[ 0 ] == "or" or linea[ 0 ] == "nor" or linea[ 0 ] == "slt" or linea[ 0 ] == "sltu" or linea[ 0 ] == "jr" or linea[ 0 ] == "srl" or linea[ 0 ] == "mult" or linea[ 0 ] == "multu" or linea[ 0 ] == "div" or linea[ 0 ] == "divu":
                    if linea[ 0 ] == "jr":
                        if linea[ 1 ] in instrucciones:
                            codigoBinario = codigoBin[ 0 ] + codigoBin[ 1 ] + "00000" + "00000" + "00000" + "001000"
                            textoBin.insert( INSERT, codigoBinario )
                        else:
                            textoBin.insert( INSERT, f"Error de Sintaxis en { linea[ 0 ] }" )
                    else:
                        if linea[ 1 ] in instrucciones and linea[ 2 ] in instrucciones and linea[ 3 ] in instrucciones:
                            codigoBinario = "000000" + codigoBin[ 2 ] + codigoBin[ 3 ] + codigoBin[ 1 ] + "00000" + codigoBin[ 0 ]
                            textoBin.insert( INSERT, codigoBinario )
                        else:
                            textoBin.insert( INSERT, f"Error de Sintaxis en { linea[ 0 ] }" )
                elif linea[ 0 ] == "sll" or linea[ 0 ] == "sra":
                    codigoBinario = "000000" + codigoBin[ 2 ] + codigoBin[ 3 ] + codigoBin[ 1 ] + "11111" + codigoBin[ 0 ]
                    textoBin.insert( INSERT, codigoBinario )
                elif linea[ 0 ] == "beq" or linea[ 0 ] == "bne":
                    #numero1 = int( input( f"Digite el numero 1 del registro { linea[ 1 ] }: " ) )
                    #numero2 = int( input( f"Digite el numero 2 del registro { linea[ 2 ] }: " ) )
                    if linea[ 1 ] in instrucciones and linea[ 2 ] in instrucciones:
                        encontroEtiqueta = 0
                        for i in range( len( etiquetas ) ):
                           if linea[ 3 ] == etiquetas[ i ][ 0 ].replace( ":", "" ):
                               encontroEtiqueta = 1
                               break
                        if encontroEtiqueta == 1:
                            etiqueta = linea[ 3 ]
                            for i in range( len( etiquetas ) ):
                                if etiqueta == etiquetas[ i ][ 0 ].replace( ":", "" ):
                                    label = int( posicionXDefecto[ 2: ] ) + ( etiquetas[ i ][ 1 ] * 4 )
                                    actual = int( posicionXDefecto[ 2: ] ) + ( index * 4 )
                                    direccion = int( ( label - ( actual + 4 ) ) / 4 )
                                    codigoBinario = codigoBin[ 0 ] + codigoBin[ 1 ] + codigoBin[ 2 ] + convertirDecToBin( direccion )
                                    textoBin.insert( INSERT, codigoBinario )
                        else:
                            textoBin.insert( INSERT, f"Error de Sintaxis en { linea[ 0 ] }" )
                    else:
                        textoBin.insert( INSERT, f"Error de Sintaxis en { linea[ 0 ] }" )
                if len( linea ) != 1:    
                    index += 1
                linea = f.readline() 
                textoBin.insert( INSERT, "\n" )
            f.close()
            f = open( archivo, 'r' )
            contador1 = 0 #variables 
            contador2 = 0 #variable n :D
            contador3 = 0 #el de contador para reinciarlo
            cantidadLineasArchivo = f.readlines()
            for i in range( len( cantidadLineasArchivo ) ):
                if cantidadLineasArchivo[ i ].strip().split()[ 0 ] == "lb" or cantidadLineasArchivo[ i ].strip().split()[ 0 ] == "lbu" or cantidadLineasArchivo[ i ].strip().split()[ 0 ] == "lh" or cantidadLineasArchivo[ i ].strip().split()[ 0 ] == "lhu" or cantidadLineasArchivo[ i ].strip().split()[ 0 ] == "lw":
                    contador3 += 5
                elif cantidadLineasArchivo[ i ].strip().split()[ 0 ] == "beq" or cantidadLineasArchivo[ i ].strip().split()[ 0 ] == "bne":
                    contador3 += 6
                elif cantidadLineasArchivo[ i ].strip().split()[ 0 ] == "j" or cantidadLineasArchivo[ i ].strip().split()[ 0 ] == "jal":
                    contador3 += 3
                elif len( cantidadLineasArchivo[ i ].strip().split() ) == 1:
                    pass
                else:
                    contador3 += 4
                try:
                    if len( cantidadLineasArchivo[ i + 1 ].strip().split() ) == 1:
                        contador1 += contador3
                        contador3 = 0
                        indexError = 1
                    elif cantidadLineasArchivo[ i + 1 ].strip().split()[ 0 ] == "j":
                        contador2 += contador3
                        contador3 = 0
                        indexError = 0
                except IndexError:
                    if indexError == 0:
                        contador2 += contador3
                        contador3 = 0
                    else:
                        contador1 += contador3
                        contador3 = 0           
            f.close()
            tiempoEjecucion = f"{ contador1 / frecuencia.get() } + { contador2 / frecuencia.get() }n"
            messagebox.showinfo( title = "Info", message = f"Tiempo de Ejecucion: { tiempoEjecucion } s" )
        else:
            messagebox.showwarning( title = "Alerta", message = "Recuerda colocar la frecuencia del reloj" )
    else:
        messagebox.showerror( title = "Error", message = "No has seleccionado ningun archivo" )

def main():
    #Iniciacion interfaz
    global programa, texto, textoBin, validar, frecuencia
    programa = Tk()
    programa.title( "Mips To Bin" )
    programa.geometry( '685x320' )
    programa.iconbitmap( "binario.ico" )
    programa.configure( background = 'light sea green' )
    #Textos
    Label( programa, text = "Juan Acosta y Maria del Mar Villaquiran", background = 'light sea green' ).place( x = 230, y = 0 )
    Label( programa, text = "Codigo Mips", background = 'light sea green' ).place( x = 100, y = 290 )
    Label( programa, text = "Codigo Binario", background = 'light sea green' ).place( x = 490, y = 290 )
    Label( programa, text = "Frecuencia", background = 'light sea green' ).place( x = 298, y = 90 )
    texto = st.ScrolledText( programa, width = 30, height = 16 )
    texto.grid( column = 0, row = 0, padx = 10, pady = 30 )
    textoBin = st.ScrolledText( programa, width = 32, height = 16 )
    textoBin.grid( column = 2, row = 0, padx = 10, pady = 30 )  
    #Entradas
    frecuencia = IntVar()
    Entry( programa, textvariable = frecuencia, width = 10 ).place( x = 298, y = 110 )
    #Botones
    Button( programa, text = "Abrir Archivo", command = abrirArchivo ).grid( column = 1, row = 0, padx = 10, pady = 20 ) 
    Button( programa, text = "Convertir", command = convertirABinario ).place( x = 300, y = 190 )
    #Ciclo
    programa.mainloop()

main()