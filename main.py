import pygame, sys, random
import time
import pygame.locals as globales
import pygame.event as eventos
import pygame.time as tiempo

import clases

pygame.init()
pygame.font.init()
#pygame.mouse.set_visible(False)

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

#*****************************VARIABLES DEL JUEGO****************************************************************************

jugadores = [
     { "nombre" : "Jugador Uno" , "tts" : None } ,
     { "nombre" : "Jugador Dos" , "tts" : None } ,
     { "nombre" : "Walter" , "tts" : None } ,
     { "nombre" : "Lilly" , "tts" : None } 
     ]

jugadorUno = clases.Jugador(pygame, "Jugador 1", True, azul, "izquierda")
jugadorDos = clases.Jugador(pygame, "Jugador 2", False, rojo, "derecha")

pelota = clases.pelota( "izquierda" )

menuInicio = clases.menu(pygame, 'INICIO')

sets = 1                        #sets a jugar
puntosPorSet = 11               #puntos a jugar por set
cambioSaque = 2                 #número de saques para hacer cambio de saque
lado = True
saque = True

puntosTotalesSet = 0

estados = ( "inicio" , "post juego" ,  "jugando" , "post nuevo set" , "nuevo set" , "pausa" , "fin" )

estado = estados[ 0 ]

tPres = { "1" : False , "esc" : False , }

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

def quit():
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
                if estado == "jugando" :
                    anotarPunto(jugadorUno)

            if evento.key == pygame.K_RIGHT:
                if estado == "jugando":
                    anotarPunto(jugadorDos)

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
