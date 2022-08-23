import pygame, sys, random
import time
import pygame.locals as globales
import pygame.event as eventos
import pygame.time as tiempo

pygame.init()
pygame.font.init()
#pygame.mouse.set_visible(False)

frames = tiempo.Clock() 
fps = 10                            #velocidad de actualización en frames por segundo
velocidadDeAnimacion = 1            #tiempo en segundos para hacer cada animación
 
ancho, alto = 1920, 1080
#obtener resolución de pantalla
infoPantalla = pygame.display.Info()
print(infoPantalla)
#eslaca de pantalla
escala = infoPantalla.current_w / ancho
print("escala: " + str(escala))
escala = .83

ventana = pygame.display.set_mode((infoPantalla.current_h, infoPantalla.current_w), pygame.FULLSCREEN)

pygame.display.set_caption( 'Marcador para tenis de mesa' )

fondo = pygame.image.load( "assets/img/fondo.jpg" )
fondo = pygame.transform.scale(fondo, ( int( ancho * escala) , int( alto * escala ) ) )

azul= pygame.image.load( "assets/img/azul.png" )
azul = pygame.transform.scale( azul, (int( azul.get_rect()[2] * escala), int( azul.get_rect()[3] * escala ) ) )
rojo = pygame.image.load( "assets/img/rojo.png" )
rojo = pygame.transform.scale( rojo, (int( rojo.get_rect()[2] * escala), int( rojo.get_rect()[3] * escala ) ) )

#***********************VARIABLES DEL JUEGO**********************************************************************************

pJugadorUno = 0                 #puntos del jugador uno
pJugadorDos = 0                 #puntos del jugador dos

sJugadorUno = 0                 #sets del jugador uno
sJugadorDos = 0                 #sets del jugador dos

nJugadorUno = "Jugador 1"       #nombre del jugador uno
nJugadorDos = "Jugador 2"       #nombre del jugador dos

sets = 1                        #sets a jugar
puntos = 11                     #puntos a jugar por set

cambioSaque = 2                 #número de saques para hacer cambio de saque
saque = False                   #define quien saca, False: Azul, True: Rojo

lado = False                    #indica el lado de cada jugador. False: Azul a la izquierda,  True: Rojo a la izquierda 

#-----------------------------FUNCIONES--------------------------------------------------------------------------------------

def mover():
    print ( "moviendo" )

def dibujarFondo():
    ventana.blit( fondo, ( 0, 0 ) )
    ventana.blit(azul, ( int( 60 * escala ), int( 60 * escala ) ) )
    ventana.blit(rojo, ( int( 1020 * escala ), int( 60 * escala ) ) )


def dibujarDatos():
    print("dibujando datos")

def dibujarMarcadores():

    fuente = pygame.font.SysFont( "Lucida Sans", int( 200 * escala ) )
    imgTexto = fuente.render( str( pJugadorUno ), True, ( 255, 255, 255 ) )
    ventana.blit( imgTexto, ( ( int( 450 + ( imgTexto.get_rect()[2] ) / 2 ), ( int( 250 * escala ) ) ) )

    fuente = pygame.font.SysFont( "Lucida Sans", int( 200 * escala ) )
    imgTexto = fuente.render( str( pJugadorDos ), True, ( 255, 255, 255 ) )
    ventana.blit( imgTexto, ( ( ( 1200 + ( imgTexto.get_rect()[2] ) / 2 ) * escala ), ( int( 250 * escala)  ) ) )

def quit():
    pygame.font.quit()
    pygame.quit()
    sys.exit()

#----------------------------------CICLO PRINCIPAL---------------------------------------------------------------------------    

while True:

    mover()
    dibujarFondo()
    dibujarDatos()
    dibujarMarcadores()


    for evento in eventos.get():

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                quit()

            if evento.key == pygame.K_LEFT:
                pJugadorUno += 1

            if evento.key == pygame.K_RIGHT:
                pJugadorDos += 1


        if evento.type == globales.QUIT:
            quit()


    pygame.display.update()

    frames.tick(fps)
