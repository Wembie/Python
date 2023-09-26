"""
Deben hacer un programa en el que se pueda leer una historia y que tenga sonidos que ambientan dicha historia.

Notas aclaratorias:

El programa debe hacer uso de la librería OpenAL.
El programa puede estar desarrollado en Python, C, C++ o Java. 
La historia debe poder leerse línea por línea, es decir, el programa debe permitir esto.
Cada línea de la historia debe tener una pieza musical o efecto de sonido adecuado a lo que se está contando y además debe estar posicionado en el espacio. Por ejemplo, si la historia dice que a lo lejos se escucha un caballo, el sonido debe escucharse lejos, si la historia dice que por detrás se acercaba una persona entonces el sonido correspondiente debe venir de atras, y si la historia narra que a la derecha hay una estampida de elefantes entonces el sonido debe escucharse por el speaker derecho de los audífonos.
No es necesaria una interfaz gráfica, pero sí deben hacer una interfaz por línea de comandos que permita ir avanzando en la historia.
La historia debe tener, al menos, 50 líneas de texto, y debe ser una historia completa, lo que significa que tenga inicio, nudo, desenlace y final.
Deben entregar el código fuente y los sonidos usados, todo empquetado en un archivo zip.
"""


import pyttsx3
import time
import pyglet

# Inicializar el motor de texto a voz
engine = pyttsx3.init()

# Definir la historia
historia = [
    "El sol comenzaba a ascender en el horizonte, arrojando sus primeros rayos de luz sobre el campamento del intrépido explorador, Wembie. Empacó sus pertenencias en su mochila y se dispuso a emprender una expedición en la selva amazónica. El sonido de los pájaros cantando llenó el aire desde todas las direcciones", "(sonidoPajaros)", "creando una atmósfera de vida exuberante y misterio. Después de horas de caminata, John llegó a un antiguo templo escondido en la espesura de la selva. Cuando se acercó a la entrada, el suelo crujía bajo sus pies debido a las hojas secas y ramas caídas.", "(sonidoHojas)", "Mientras exploraba el interior del templo, una corriente de aire sopló desde la izquierda,", "(sonidoViento)", "provocando un eco en las paredes de piedra.", "John encontró una serie de jeroglíficos en la pared y comenzó a descifrarlos lentamente. A medida que leía, un ruido sordo de agua corriente resonó desde la derecha", "(sonidoRio)", "indicando la presencia de un río subterráneo. Continuó su búsqueda, y justo cuando parecía estar cerca de descubrir el misterio del templo, un susurro inquietante se escuchó detrás de él.", "(sonidoSusurro)", "Con valentía, John decidió seguir el susurro y descubrió una sala secreta detrás de una puerta oculta. Dentro, encontró un tesoro perdido hace siglos, brillando bajo la tenue luz de una antorcha.", "(sonidoTesoro)", "Pero no estaba solo; una serpiente venenosa se deslizó hacia él desde el centro de la sala.", "(sonidoSerpiente)", "Después de una intensa lucha, John logró evitar el ataque de la serpiente y escapar del templo con el tesoro en mano. A medida que salía, el sonido de la selva y los pájaros se hizo más fuerte, indicando que había regresado al exterior.", "(sonidoSelva)", "John volvió a su campamento, triunfante y lleno de historias para contar. Mientras se sentaba junto a su fogata", "(sonidoFogata)", "la noche cayó y las estrellas brillaron en el cielo.", "(sonidoEstrellas)", "Fin."
]

# Configurar el motor de texto a voz
engine.setProperty('rate', 150)  # Velocidad de lectura
engine.setProperty('volume', 1.0)  # Volumen

# Cargar archivos de sonido en objetos pyglet.media.Player
efectos_sonido = {
    "(sonidoPajaros)": pyglet.media.load("sonidoPajaros.mp3"),
    "(sonidoHojas)": pyglet.media.load("sonidoHojas.mp3"),
    "(sonidoViento)": pyglet.media.load("sonidoViento.mp3"),
    "(sonidoRio)": pyglet.media.load("sonidoRio.mp3"),
    "(sonidoSusurro)": pyglet.media.load("sonidoSusurro.mp3"),
    "(sonidoTesoro)": pyglet.media.load("sonidoTesoro.mp3"),
    "(sonidoSerpiente)": pyglet.media.load("sonidoSerpiente.mp3"),
    "(sonidoSelva)": pyglet.media.load("sonidoSelva.mp3"),
    "(sonidoEstrellas)": pyglet.media.load("sonidoEstrellas.mp3"),
    "(sonidoFogata)": pyglet.media.load("sonidoFogata.mp3"),
}

# Leer cada párrafo
for parrafo in historia:
    # Luego, narrar el párrafo o reproducir el efecto de sonido
    if parrafo.startswith("(sonido"):
        # Crear un reproductor de sonido con soporte 3D
        player = pyglet.media.Player()
        player.volume = 1.0  # Volumen (0.0 a 1.0)
        sonido = efectos_sonido.get(parrafo, None)
        if sonido:
            # Configurar la posición 3D del sonido (coordenadas x, y, z)
            if parrafo == "(sonidoPajaros)":
                sonido_position = (0, 0, 0)
            elif parrafo == "(sonidoHojas)":
                sonido_position = (0, -1, 0)
            elif parrafo == "(sonidoViento)":
                sonido_position = (-1, 0, 0)
            elif parrafo == "(sonidoRio)":
                sonido_position = (1, 0, 0)
            elif parrafo == "(sonidoSusurro)":
                sonido_position = (0, 0, -1)
            elif parrafo == "(sonidoTesoro)":
                sonido_position = (0, 0, 1)
            elif parrafo == "(sonidoSerpiente)":
                sonido_position = (0, 0, 0)
            elif parrafo == "(sonidoSelva)":
                sonido_position = (0, 0, 0)
            elif parrafo == "(sonidoFogata)":
                sonido_position = (0, 0, 1)
            elif parrafo == "(sonidoEstrellas)":
                sonido_position = (0, 1, 0)
            player.position = sonido_position
            # Reproducir el efecto de sonido
            player.queue(sonido)
            player.play()
            time.sleep(5.5)  # Pausa de 5.5 segundos entre párrafos
    else:
        engine.say(parrafo)
        engine.runAndWait()

# Detener la reproducción después de que se complete la historia
pyglet.app.exit()
