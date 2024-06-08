"""
Codigo Morse 'SOS': ... --- ...
Codigo Morse 'JOB DONE ? FINE !': .--- --- -...  -.. --- -. .  ..--..  ..-. .. -. . -.-.--
"""

def convertirANormal( frase ):
    morse = {
    '.-': 'A',     '-...': 'B',    '-.-.': 'C',
    '-..': 'D',    '.': 'E',       '..-.': 'F',
    '--.': 'G',    '....': '',    '..': 'I',
    '.---': 'J',   '-.-': 'K',     '.-..': 'L',
    '--': 'M',     '-.': 'N',      '---': 'O',
    '.--.': 'P',   '--.-': 'Q',    '.-.': 'R',
    '...': 'S',    '-': 'T',       '..-': 'U',
    '...-': 'V',   '.--': 'W',     '-..-': 'X',
    '-.--': 'Y',   '--..': 'z',    '.----': '1',
    '..---': '2',  '...--': '3',   '....-': '4',
    '.....': '5',  '-....': '6',   '--...': '7',
    '---..': '8',  '----.': '9',   '-----': '0',
    '.-.-.-': '.', '--..--': ',',  '---...': ':',
    '-.-.-.': ';', '..--..': '?',  '-.-.--': '!',
    '.-..-.': '"', '.----.': "'",  '.-.-.': '+',
    '-....-': '-', '-..-.': '/',   '-...-': '=',
    '..--.-': '_', '...-..-': '$', '.--.-.': '@',
    '.-...': '&',  ' ': ' ', '': ' ' }
    fraseConvertida = ""
    letra = ""
    for letraFrase in frase: 
        if letraFrase == ' ':
            fraseConvertida += morse[ letra ]
            letra = ""
        else:
            letra += letraFrase
    return fraseConvertida

def main():
    limite = 2000
    vecesARepetir = int( input( "Digite la cantidad de frases a digitar: " ) )
    for numero in range( vecesARepetir ):
        fraseAConvertir = input( f"Digita la frase en morse a convertir # { numero + 1 }: " )
        if len( fraseAConvertir ) <= limite:
            print( f"\nMessage #{ numero + 1 }:" )
            print( f"{ convertirANormal( fraseAConvertir + ' ' ) }\n" )
        else:
            print( "La frase no puede sobrepasar el limite de 2000 caracteres" )

main()