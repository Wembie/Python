from email.message import EmailMessage 

import marshal
import smtplib 
import time

def preguntarNumero( inicio, final, recuadro ): 
    while True:
        try:
            opcion = int( input( f"\n───> Digite el numero deseado { recuadro }: " ) )
        except ValueError:
            print( "\nSolo se recibe numeros enteros" )
        else:
            if opcion >= inicio and opcion <= final:
                print( "" )
                return opcion
            else:
                print( "\nNumero invalido" )
                print( "Por favor digitelo nuevamente" )

def preguntarNumeroNormal( recuadro, numero ):
    if numero == 0:
        while True:
            try:
                opcion = int( input( f"───> { recuadro }" ) )
            except ValueError:
                    print( "\nSolo se recibe numeros enteros\n" )
            else:
                if opcion > 0:
                    return opcion
                else:
                    print( "\nEl numero a digitar debe ser mayor a 0\n" )
    elif numero == 1:
        while True:
            try:
                opcion = float( input( f"───> { recuadro }: " ) )
            except ValueError:
                    print( "\nSolo se recibe numeros flotantes\n" )
            else:
                if opcion > 0:
                    return opcion
                else:
                    print( "\nEl numero a digitar debe ser mayor a 0\n" )
    elif numero == 2:
        while True:
            try:
                opcion = int( input( f"───> {recuadro}: " ) )
            except ValueError:
                    print( "\nSolo se recibe numeros enteros\n" )
            else:
                return opcion
    elif numero == 3:
        while True:
            try:
                opcion = float( input( f"───> { recuadro }: " ) )
            except ValueError:
                    print( "\nSolo se recibe numeros flotantes\n" )
            else:
                return opcion
    elif numero == 4:
        while True:
            try:
                opcion = int( input( f"{ recuadro }" ) )
            except ValueError:
                    print( "\nSolo se recibe numeros enteros\n" )
            else:
                if opcion > 0:
                    return opcion
                else:
                    print( "\nEl numero a digitar debe ser mayor a 0\n" )

def guardarArchivoDatos( datos, nombre ):
    archivo = open( f"Datos/{ nombre }/{ nombre }", "bw" )
    marshal.dump( datos, archivo )
    archivo.close()

def enviarCorreo( asunto, mensajito ): 
    emailEnviador = "example@hotmail.com" 
    #emailRecibidor = "" 
    emailRecibidor = "example@hotmail.com" 
    email_smtp = "smtp-mail.outlook.com" 
    email_password = "password123" 
    mensaje = EmailMessage() 
    mensaje[ 'Subject' ] = asunto
    mensaje[ 'From' ] = emailEnviador
    mensaje[ 'To' ] = emailRecibidor 
    mensaje.set_content( mensajito ) 
    servidor = smtplib.SMTP( email_smtp, port = 587 ) 
    servidor.ehlo() 
    servidor.starttls() 
    servidor.login( emailEnviador, email_password ) 
    servidor.send_message( mensaje ) 
    servidor.quit()

def espera( mensaje ):
    puntos = "..."
    for i in range( 4 ):
        print( mensaje + puntos[ :i ], end = '\r' )
        time.sleep( 0.5 )
