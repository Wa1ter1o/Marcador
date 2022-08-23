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

medidas = { "medioX" : 960, "cuartoX" : 480, "tresCuartosX" : 1440 }

iu = { 
    "fuente" : "OCR A Extended", 
    "tFNombre" : 100, "tFMarcador" : 475, "tFSets" : 200, 
    "yNombre" : 125, "yMarcador" : 225, "ySets" : 700, 
    "compSets" : 300
    }

jugadorUno = { "puntos" : 0, "sets" : 0, "nombre" : "Jugador 1", "saque" : True, "lado" : True, "color" : True }
jugadorDos = { "puntos" : 0, "sets" : 0, "nombre" : "Jugador 2", "saque" : False, "lado" : False, "color" : False }

sets = 1                        #sets a jugar
puntos = 11                     #puntos a jugar por set
cambioSaque = 2                 #número de saques para hacer cambio de saque

#-----------------------------FUNCIONES--------------------------------------------------------------------------------------


def dibujarFondo():
    ventana.blit( fondo, ( 0, 0 ) )
    ventana.blit(azul, ( int( 60 * escala ), int( 60 * escala ) ) )
    ventana.blit(rojo, ( int( 1020 * escala ), int( 60 * escala ) ) )


def dibujarDatos():

    # Dibujado de nombre de jugador izquierdo
    fuente = pygame.font.SysFont( iu["fuente"], int( iu["tFNombre"] * escala ) )
    imgTexto = fuente.render( str( jugadorUno["nombre"] ), True, ( 255, 255, 255 ) )
    ventana.blit( imgTexto, ( ( int( ( medidas["cuartoX"] - ( imgTexto.get_rect()[2] / 2) ) * escala )), ( int( iu["yNombre"] * escala ) ) ) )

    # Dibujado de nombre de jugador derecho
    fuente = pygame.font.SysFont( iu["fuente"], int( iu["tFNombre"] * escala ) )
    imgTexto = fuente.render( str( jugadorDos["nombre"] ), True, ( 255, 255, 255 ) )
    ventana.blit( imgTexto, ( ( int( ( medidas["tresCuartosX"] - ( imgTexto.get_rect()[2] / 2) ) * escala )), ( int( iu["yNombre"] * escala ) ) ) )

def dibujarMarcadores():

    # Dibujado de marcador izqiuerdo
    fuente = pygame.font.SysFont( iu["fuente"], int( iu["tFMarcador"] * escala ) )
    imgTexto = fuente.render( str( jugadorUno["puntos"] ), True, ( 255, 255, 255 ) )
    ventana.blit( imgTexto, ( ( int( ( medidas["cuartoX"] - ( imgTexto.get_rect()[2] / 2) ) * escala )), ( int( iu["yMarcador"] * escala ) ) ) )

    # Dibujado de marcador derecho
    fuente = pygame.font.SysFont( iu["fuente"], int( iu["tFMarcador"] * escala ) )
    imgTexto = fuente.render( str( jugadorDos["puntos"] ), True, ( 255, 255, 255 ) )
    ventana.blit( imgTexto, ( ( int( ( medidas["tresCuartosX"] - ( imgTexto.get_rect()[2] / 2) ) * escala )), ( int( iu["yMarcador"] * escala ) ) ) )

    # Dibujado de sets izquierdo
    fuente = pygame.font.SysFont( iu["fuente"], int( iu["tFSets"] * escala ) )
    imgTexto = fuente.render( str( jugadorUno["sets"] ), True, ( 255, 255, 255 ) )
    ventana.blit( imgTexto, ( ( int( ( iu["compSets"] + medidas["cuartoX"] - ( imgTexto.get_rect()[2] / 2) ) * escala )), ( int( iu["ySets"] * escala ) ) ) )

    # Dibujado de sets izquierdo
    fuente = pygame.font.SysFont( iu["fuente"], int( iu["tFSets"] * escala ) )
    imgTexto = fuente.render( str( jugadorDos["sets"] ), True, ( 255, 255, 255 ) )
    ventana.blit( imgTexto, ( ( int( ( iu["compSets"] - medidas["tresCuartosX"] - ( imgTexto.get_rect()[2] / 2) ) * escala )), ( int( iu["ySets"] * escala ) ) ) )

def modificarPuntos(jugador, incremental):


    if jugador == 1:
        jugadorUno["puntos"] += incremental

    if jugador == 2:
        jugadorDos["puntos"] += incremental

def quit():
    pygame.font.quit()
    pygame.quit()
    sys.exit()

#----------------------------------CICLO PRINCIPAL---------------------------------------------------------------------------    

while True:

    dibujarFondo()
    dibujarDatos()
    dibujarMarcadores()


    for evento in eventos.get():

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                quit()

            if evento.key == pygame.K_LEFT:
                modificarPuntos( 1, 1 )

            if evento.key == pygame.K_RIGHT:
                modificarPuntos( 2, 1 ) 


        if evento.type == globales.QUIT:
            quit()


    pygame.display.update()

    frames.tick(fps)
