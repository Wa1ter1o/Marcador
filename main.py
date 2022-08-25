import pygame, sys, random
import time
import pygame.locals as globales
import pygame.event as eventos
import pygame.time as tiempo

import jugador

pygame.init()
pygame.font.init()
#pygame.mouse.set_visible(False)

frames = tiempo.Clock() 
fps = 30                            #velocidad de actualización en frames por segundo
velAnim = 1                         #tiempo en segundos para hacer cada animación
pasoAnim = 3                        #incremental de movimiento para todas las animaciones en pixels

ancho, alto = 1920, 1080
#obtener resolución de pantalla
infoPantalla = pygame.display.Info()
#print(infoPantalla)
#escala de pantalla
escala = infoPantalla.current_w / ancho
print("escala: " + str(escala))
#escala = 0.83

ventana = pygame.display.set_mode( ( int( ancho  ), int( alto  ) ), pygame.FULLSCREEN)
canvas = pygame.Surface( (ancho, alto) )

print( "canvas: " , canvas.get_rect()[2], canvas.get_rect()[3])

pygame.display.set_caption( 'Marcador para tenis de mesa' )

#-------------------------Cargando Imágenes----------------------------------------------------------------------------------

fondoOriginal = pygame.image.load( "assets/img/fondo.jpg" )
fondo = pygame.transform.scale(fondoOriginal, ( int( ancho ) , int( alto  ) ) )

azul = pygame.image.load( "assets/img/azul.png" )
rojo = pygame.image.load( "assets/img/rojo.png" )
color = True

#***********************VARIABLES DEL INTERFÁZ DE USUARIO********************************************************************



#*****************************VARIABLES DEL JUEGO****************************************************************************

jugadorUno = jugador.Jugador(pygame, "Jugador 1", True, azul, "izquierda")
jugadorDos = jugador.Jugador(pygame, "Jugador 2", False, rojo, "derecha")

sets = 1                        #sets a jugar
puntos = 11                     #puntos a jugar por set
cambioSaque = 2                 #número de saques para hacer cambio de saque
lado = True



#-----------------------------FUNCIONES--------------------------------------------------------------------------------------

def mover():
    jugadorUno.mover(pasoAnim)
    jugadorDos.mover(pasoAnim)

def dibujarFondo():

    canvas.blit( fondo, ( 0, 0 ) )     #dibujar fondo


def dibujarMarcadores():

    # Dibujado de marcador izquierdo
    fuente = pygame.font.SysFont( iu["fuente"], int( iu["tFMarcador"]  ) )
    imgTexto = fuente.render( str( jugadorUno["puntos"] ), True, ( 255, 255, 255 ) )
    canvas.blit( imgTexto, 
        ( ( int( ( medidas["cuartoX"] - ( ( imgTexto.get_rect()[2]  ) / 2) + iu["compMarcos"] )  )), 
        ( int( iu["yMarcador"]  ) ) ) )

    # Dibujado de marcador derecho
    fuente = pygame.font.SysFont( iu["fuente"], int( iu["tFMarcador"]  ) )
    imgTexto = fuente.render( str( jugadorDos["puntos"] ), True, ( 255, 255, 255 ) )
    canvas.blit( imgTexto, 
        ( ( int( ( medidas["tresCuartosX"] - ( ( imgTexto.get_rect()[2]  ) / 2) - + iu["compMarcos"] )  )), 
        ( int( iu["yMarcador"]  ) ) ) )

    # Dibujado de sets izquierdo
    fuente = pygame.font.SysFont( iu["fuente"], int( iu["tFSets"]  ) )
    imgTexto = fuente.render( str( jugadorUno["sets"] ), True, ( 255, 255, 255 ) )
    canvas.blit( imgTexto, ( ( int( ( iu["compSets"] + medidas["cuartoX"] - ( imgTexto.get_rect()[2] / 2) )  )), 
        ( int( iu["ySets"]  ) ) ) )

    # Dibujado de sets derecho
    fuente = pygame.font.SysFont( iu["fuente"], int( iu["tFSets"]  ) )
    imgTexto = fuente.render( str( jugadorDos["sets"] ), True, ( 255, 255, 255 ) )
    canvas.blit( imgTexto, ( ( int( ( - iu["compSets"] + medidas["tresCuartosX"] - ( imgTexto.get_rect()[2] / 2) )  )), 
        ( int( iu["ySets"]  ) ) ) )

def dibujarCuadrados():

    pygame.draw.rect(canvas, ( 200, 200, 200 ), ( 0, 0, medidas["medioX"] , alto/2 ), 5 )
    pygame.draw.rect(canvas, ( 200, 200, 200 ), ( medidas["cuartoX"] , 0, medidas["medioX"]  , alto  ), 5 )


def comprobarReglas():
    print ("comprobando reglas")


def anotarPunto(jugador):

    jugador.anotarPunto()

    comprobarReglas()

def cambiarLado():
    jugadorUno.cambiarLado()
    jugadorDos.cambiarLado()

def cambiarColor():

    if color:
        jugadorUno.cambiarColor(rojo)
        jugadorDos.cambiarColor(azul)
    else:
        jugadorUno.cambiarColor(azul)
        jugadorDos.cambiarColor(rojo)

    color = not color

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
    #dibujarPelota()
    #dibujarCuadrados()


    for evento in eventos.get():

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                quit()

            if evento.key == pygame.K_LEFT:
                anotarPunto(jugadorUno)

            if evento.key == pygame.K_RIGHT:
                anotarPunto(jugadorDos) 

            if evento.key == pygame.K_SPACE:
                cambiarLado()

            if evento.key == pygame.K_c:
                cambiarColor()


        if evento.type == globales.QUIT:
            quit()

    dibujarCanvas()

    pygame.display.update()

    frames.tick(fps)
