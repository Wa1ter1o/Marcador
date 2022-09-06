import pygame, sys, random
import time
import pygame.locals as globales
import pygame.event as eventos
import pygame.time as tiempo
from pygame import mixer

import clases

pygame.init()
pygame.font.init()
pygame.mixer.init()

pygame.mouse.set_visible(False)

frames = tiempo.Clock() 
fps = 10                            #velocidad de actualización en frames por segundo
velAnim = 1                         #tiempo en segundos para hacer cada animación
pasoAnim = 80                       #incremental de movimiento para todas las animaciones en pixels

ancho, alto = 1920, 1080
#obtener resolución de pantalla
infoPantalla = pygame.display.Info()
#print(infoPantalla)
#escala de pantalla
escala = infoPantalla.current_w / ancho
print("escala: " + str(escala))
escala = 0.7

ventana = pygame.display.set_mode( ( int( ancho * escala  ), int( alto * escala ) ) )
canvas = pygame.Surface( (ancho, alto) )

pygame.display.set_caption( 'Marcador para tenis de mesa' )

#-------------------------Cargando Imágenes----------------------------------------------------------------------------------

fondoOriginal = pygame.image.load( "assets/img/fondo.jpg" )
fondo = pygame.transform.scale(fondoOriginal, ( int( ancho ) , int( alto  ) ) )

azul = pygame.image.load( "assets/img/azul.png" )
rojo = pygame.image.load( "assets/img/rojo.png" )
color = True

#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& JUGADORES $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

jugadores = [
     { "nombre" : "Alejandro" , "tts" : mixer.Sound('assets/sonidos/nombres/Alejandro.wav') } ,
     { "nombre" : "Diego" , "tts" : mixer.Sound('assets/sonidos/nombres/Diego.wav') } ,
     { "nombre" : "Javi" , "tts" : mixer.Sound('assets/sonidos/nombres/Javi.wav') } ,
     { "nombre" : "Jugador Uno" , "tts" : mixer.Sound('assets/sonidos/nombres/Jugador uno.wav') } ,
     { "nombre" : "Jugador Dos" , "tts" : mixer.Sound('assets/sonidos/nombres/Jugador dos.wav') } ,
     { "nombre" : "Lilly" , "tts" : mixer.Sound('assets/sonidos/nombres/Lilly.wav') } ,
     { "nombre" : "Pablo" , "tts" : mixer.Sound('assets/sonidos/nombres/Pablo.wav') } ,
     { "nombre" : "Walter" , "tts" : mixer.Sound('assets/sonidos/nombres/Walter.wav') } ,
     { "nombre" : "Willy" , "tts" : mixer.Sound('assets/sonidos/nombres/Willy.wav') } ,
     { "nombre" : "William" , "tts" : mixer.Sound('assets/sonidos/nombres/William.wav') } 
     ]

nombres = []
for jugador in jugadores:
    nombres.append(jugador['nombre'])

#*****************************VARIABLES DEL JUEGO****************************************************************************

jugadorUno = clases.Jugador(pygame, "Jugador Uno", mixer.Sound('assets/sonidos/nombres/Jugador uno.wav'),True, azul, "izquierda")
jugadorDos = clases.Jugador(pygame, "Jugador Dos", mixer.Sound('assets/sonidos/nombres/Jugador dos.wav') ,False, rojo, "derecha")

pelota = clases.pelota( "izquierda" )


sets = 1                        #sets a jugar
puntosPorSet = 11               #puntos a jugar por set
cambioSaque = 2                 #número de saques para hacer cambio de saque
lado = True                     #define de que lado se encuentra cada jugador
saque = True                    #si es True el saque le corresponde al jugador uno


puntosTotalesSet = 0

estados = ( "inicio" , "post juego" ,  "jugando" , "post nuevo set" , "nuevo set" , "pausa" , "fin" )

estado = estados[ 0 ]

tPres = { "1" : False , "esc" : False , }

#////////////////////////////// LISTAS DE MENÚ //////////////////////////////////////////////////////////////////////////////

indicesMenu = { 'inicio' : 0 }

datosInicio = [
    {
        'titulo' : 'Jugador 1', 'dato' : jugadorUno.nombre, 'datos' : nombres, 'indice' : 0
    },
    {
        'titulo' : 'Jugador 2', 'dato' : jugadorDos.nombre, 'datos' : nombres, 'indice' : 0
    },
    {
        'titulo' : 'Sets' , 'dato' : sets
    },
    {
        'titulo' : 'Pts. Por Set' , 'dato' : puntosPorSet
    },
    {
        'titulo' : 'Saque Inicial' , 'dato' : jugadorUno.nombre, 'datos' : [jugadorUno.nombre, jugadorDos.nombre, 'Sorteo'], 'indice' : 0
    }

]

menuInicio = clases.menu(pygame, 'INICIO', 'Espacio Para Continuar' ,datosInicio, indicesMenu['inicio'] )

#-----------------------------FUNCIONES--------------------------------------------------------------------------------------

def mover():
    jugadorUno.mover(pasoAnim)
    jugadorDos.mover(pasoAnim)

    pelota.mover(pasoAnim)

def dibujarFondo():

    canvas.blit( fondo, ( 0, 0 ) )

def dibujarJugadores():
    canvas.blit(jugadorUno.generarImagen(), jugadorUno.pos)
    canvas.blit(jugadorDos.generarImagen(), jugadorDos.pos)

    pygame.draw.circle( canvas, ( 250, 250, 250), ( pelota.pos ), 100 )

def dibujarMenu() :

    if estado == estados[ 0 ] :
        canvas.blit( menuInicio.generarImagen(), menuInicio.pos )


def comprobarReglas():


    if ( puntosPorSet - jugadorUno.puntos <= 1 ) and ( puntosPorSet - jugadorDos.puntos <= 1 ) :
        cambiarSaque()
    elif puntosTotalesSet % cambioSaque == 0:
        cambiarSaque()

    pInvParaGanar = ( puntosPorSet + 1 ) / 2 + 1
    if ( jugadorUno.puntos == pInvParaGanar or jugadorDos.puntos == pInvParaGanar) and \
        ( jugadorUno.puntos == 0 or jugadorDos.puntos == 0 ) :
        anotarSet()

    if ( (jugadorUno.puntos >= puntosPorSet ) or ( jugadorDos.puntos >= puntosPorSet ) ) \
        and abs( jugadorUno.puntos - jugadorDos.puntos ) >= 2 :
        anotarSet()


def anotarPunto(jugador):
    global puntosTotalesSet

    jugador.anotarPunto()

    puntosTotalesSet += 1

    comprobarReglas()

def anotarSet():

    if jugadorUno.puntos > jugadorDos.puntos :
        jugadorUno.anotarSet()

    elif jugadorDos.puntos > jugadorUno.puntos :
        jugadorDos.anotarSet()

    iniciarMarcadores()

def iniciarMarcadores():
    global puntosTotalesSet

    jugadorUno.puntos = 0
    jugadorDos.puntos = 0
    puntosTotalesSet = 0

def cambiarLado():
    jugadorUno.cambiarLado()
    jugadorDos.cambiarLado()

    pelota.cambiarLado()

def cambiarColor():
    global color

    if color:
        jugadorUno.cambiarColor(rojo)
        jugadorDos.cambiarColor(azul)
    else:
        jugadorUno.cambiarColor(azul)
        jugadorDos.cambiarColor(rojo)

    color = not color

def cambiarSaque():
    global saque

    jugadorUno.saque = not jugadorUno.saque
    jugadorDos.saque = not jugadorDos.saque

    pelota.cambiarLado()

def dibujarCanvas():

    canvasEscalado = pygame.transform.scale( canvas, ( int( ancho * escala ), int( alto * escala ) ) )
    ventana.blit( canvasEscalado, ( 0, 0 ) )

def procesarDerecha():
    global sets, puntosPorSet

    #Manejando menú inicio
    if estado == estados[0]:

        if indicesMenu['inicio'] == 0:

            if datosInicio[0]['indice'] < len(datosInicio[0]['datos']) - 1 :

                datosInicio[0]['indice'] += 1

            else:

                datosInicio[0]['indice'] = 0

            jugadorUno.nombre = jugadores[datosInicio[0]['indice']]['nombre']
            jugadorUno.tts = jugadores[datosInicio[0]['indice']]['tts']
            jugadorUno.tts.play()
            datosInicio[0]['dato'] = jugadorUno.nombre

        if indicesMenu['inicio'] == 1:

            if datosInicio[1]['indice'] < len(datosInicio[1]['datos']) - 1 :

                datosInicio[1]['indice'] += 1

            else:

                datosInicio[1]['indice'] = 0

            jugadorDos.nombre = jugadores[datosInicio[1]['indice']]['nombre']
            jugadorDos.tts = jugadores[datosInicio[1]['indice']]['tts']
            jugadorDos.tts.play()
            datosInicio[1]['dato'] = jugadorDos.nombre

        if indicesMenu['inicio'] == 2:
            
            if sets < 21:
                sets += 2   
                datosInicio[2]['dato'] = sets

        if indicesMenu['inicio'] == 3:
            
            if puntosPorSet < 21:
                puntosPorSet += 2
                datosInicio[3]['dato'] = puntosPorSet

def procesarIzquierda():
    global sets, puntosPorSet

    if estado == estados[0]:

        if indicesMenu['inicio'] == 0:

            if datosInicio[0]['indice'] > 0 :

                datosInicio[0]['indice'] -= 1

            else:

                datosInicio[0]['indice'] = len(datosInicio[0]['datos']) - 1

            jugadorUno.nombre = jugadores[datosInicio[0]['indice']]['nombre']
            jugadorUno.tts = jugadores[datosInicio[0]['indice']]['tts']
            jugadorUno.tts.play()
            datosInicio[0]['dato'] = jugadorUno.nombre

        if indicesMenu['inicio'] == 1:

            if datosInicio[1]['indice'] > 0 :

                datosInicio[1]['indice'] -= 1
                
            else:

                datosInicio[1]['indice'] = len(datosInicio[1]['datos']) - 1

            jugadorDos.nombre = jugadores[datosInicio[1]['indice']]['nombre']
            jugadorDos.tts = jugadores[datosInicio[1]['indice']]['tts']
            jugadorDos.tts.play()
            datosInicio[1]['dato'] = jugadorDos.nombre

        #Sets
        if indicesMenu['inicio'] == 2:
            
            if sets > 1:
                sets -= 2
                datosInicio[2]['dato'] = sets

        #Puntos por set
        if indicesMenu['inicio'] == 3:
            
            if puntosPorSet > 7:
                puntosPorSet -= 2
                datosInicio[3]['dato'] = puntosPorSet

def procesarAbajo():

    if estado == estados[0]:

        if indicesMenu['inicio'] < len(datosInicio) - 1:

            indicesMenu['inicio'] += 1

        else:
            indicesMenu['inicio'] = 0

        menuInicio.indice = indicesMenu['inicio']
            
def procesarArriba():

    if estado == estados[0]:

        if indicesMenu['inicio'] > 0 :

            indicesMenu['inicio'] -= 1

        else:
            indicesMenu['inicio'] = len(datosInicio) - 1

        menuInicio.indice = indicesMenu['inicio']

def quit():
    pygame.mixer.quit()
    pygame.font.quit()
    pygame.quit()
    sys.exit()

#----------------------------------CICLO PRINCIPAL---------------------------------------------------------------------------    

while True:

    mover()
    dibujarFondo()
    dibujarJugadores()
    dibujarMenu()

    for evento in eventos.get():

        if evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_1:
                tPres["1"] = True

            if evento.key == pygame.K_ESCAPE:
                tPres["esc"] = True

            if evento.key == pygame.K_LEFT:
                procesarIzquierda()

            if evento.key == pygame.K_RIGHT:
                procesarDerecha()

            if evento.key == pygame.K_DOWN:
                procesarAbajo()

            if evento.key == pygame.K_UP:
                procesarArriba()

            if evento.key == pygame.K_SPACE:
                if estado == "jugando":
                    cambiarLado()

            if evento.key == pygame.K_c:
                if estado == "jugando":
                    cambiarColor()

            if evento.key == pygame.K_s:
                if estado == "jugando":
                    cambiarSaque()

        if evento.type == pygame.KEYUP:

            if evento.key == pygame.K_1:
                tPres["1"] = False

            if evento.key == pygame.K_ESCAPE:
                tPres["esc"] = False

        if evento.type == globales.QUIT:
            quit()

    if tPres["1"] and tPres["esc"]:
        quit()

    dibujarCanvas()

    pygame.display.update()

    frames.tick(fps)
