import marshal
import os

def guardar( datos ):
    archivo = open( "Datos/datosBatallas", "bw" )
    marshal.dump( datos, archivo )
    archivo.close()

def cargar():
    datosBatallas = {}
    if os.path.exists( "Datos/datosBatallas" ):
        archivo = open( f"Datos/datosBatallas", "br" )
        datosBatallas = marshal.load( archivo )
        archivo.close()
    else:
        guardar( datosBatallas )
    return datosBatallas