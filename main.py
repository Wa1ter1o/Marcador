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

#***********************VARIABLES DEL INTERFÁZ DE USUARIO********************************************************************

medidas = { "medioX" : 960, "cuartoX" : 480, "tresCuartosX" : 1440 }

iu = { 
    "fuente" : "OCR A Extended", 
    "tFNombre" : 100, "tFMarcador" : 475, "tFSets" : 250, 
    "yNombre" : 125, "yMarcador" : 225, "ySets" : 650, 
    "compSets" : 300, "compMarcos" : 20
    }

#*****************************VARIABLES DEL JUEGO****************************************************************************

jugadorUno = { "puntos" : 0, "sets" : 0, "nombre" : "Jugador 1", "saque" : True, "color" : azul }
jugadorDos = { "puntos" : 0, "sets" : 0, "nombre" : "Jugador 2", "saque" : False, "color" : rojo }

sets = 1                        #sets a jugar
puntos = 11                     #puntos a jugar por set
cambioSaque = 2                 #número de saques para hacer cambio de saque
lado = True



#-----------------------------FUNCIONES--------------------------------------------------------------------------------------


def dibujarFondo():
    canvas.blit( fondo, ( 0, 0 ) )     #dibujar fondo

    # dibujar marco de marcador izquierdo

    if lado:
        canvas.blit(jugadorUno["color"], ( 
            int( ( medidas["cuartoX"] - ( ( jugadorUno["color"].get_rect()[2] ) / 2 ) + iu["compMarcos"] )  ),
            int( 60  ) ) )

        # dibujar marco de marcador derecho
        canvas.blit(jugadorDos["color"], ( 
            int( ( medidas["tresCuartosX"] - ( ( jugadorDos["color"].get_rect()[2] ) / 2 ) - iu["compMarcos"] )  ), 
            int( 60  ) ) )

    else:

        canvas.blit(jugadorDos["color"], ( 
            int( ( medidas["cuartoX"] - ( ( jugadorDos["color"].get_rect()[2] ) / 2 ) + iu["compMarcos"] )  ),
            int( 60  ) ) )

        # dibujar marco de marcador derecho
        canvas.blit(jugadorUno["color"], ( 
            int( ( medidas["tresCuartosX"] - ( ( jugadorUno["color"]()[2] ) / 2 ) - iu["compMarcos"] )  ), 
            int( 60  ) ) )



def dibujarDatos():

    # Dibujado de nombre de jugador izquierdo
    fuente = pygame.font.SysFont( iu["fuente"], int( iu["tFNombre"]  ) )
    imgTexto = fuente.render( str( jugadorUno["nombre"] ), True, ( 255, 255, 255 ) )
    canvas.blit( imgTexto, 
        ( ( int( ( medidas["cuartoX"] - ( ( imgTexto.get_rect()[2]  ) / 2) + iu["compMarcos"] )  )), 
        ( int( iu["yNombre"]  ) ) ) )

    # Dibujado de nombre de jugador derecho
    fuente = pygame.font.SysFont( iu["fuente"], int( iu["tFNombre"]  ) )
    imgTexto = fuente.render( str( jugadorDos["nombre"] ), True, ( 255, 255, 255 ) )
    canvas.blit( imgTexto, ( ( int( ( medidas["tresCuartosX"] - ( imgTexto.get_rect()[2] / 2) )  )), 
        ( int( iu["yNombre"]  ) ) ) )

    # Dibujando pelota a quien corresponda hacer el saque

    if jugadorUno['saque'] :
        pygame.draw.circle( canvas, ( 250, 250, 250 ), ( medidas['medioX'] - 725, iu['ySets'] + 125 ), 100)
    else:
        pygame.draw.circle( canvas, ( 250, 250, 250 ), ( medidas['medioX'] + 725, iu['ySets'] + 125 ), 100)

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


def modificarPuntos(jugador, incremental):

    if jugador == 1:
        jugadorUno["puntos"] += incremental

    if jugador == 2:
        jugadorDos["puntos"] += incremental

    comprobarReglas()

def cambiarLado():
    global lado
    lado = not lado

def cambiarColor():
    if jugadorUno["color"] == azul:
        jugadorUno["color"] = rojo
        jugadorDos["color"] = azul

    elif jugadorUno["color"] == rojo:
        jugadorUno["color"] = azul
        jugadorDos["color"] = rojo

def dibujarCanvas():

    canvasEscalado = pygame.transform.scale( canvas, ( int( ancho * escala ), int( alto * escala ) ) )
    ventana.blit( canvasEscalado, ( 0, 0 ) )

def quit():
    pygame.font.quit()
    pygame.quit()
    sys.exit()

#----------------------------------CICLO PRINCIPAL---------------------------------------------------------------------------    

while True:

    dibujarFondo()
    dibujarDatos()
    dibujarMarcadores()
    #dibujarCuadrados()


    for evento in eventos.get():

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                quit()

            if evento.key == pygame.K_LEFT:
                modificarPuntos( 1, 1 )

            if evento.key == pygame.K_RIGHT:
                modificarPuntos( 2, 1 ) 

            if evento.key == pygame.K_SPACE:
                cambiarLado()

            if evento.key == pygame.K_c:
                cambiarColor()


        if evento.type == globales.QUIT:
            quit()

    dibujarCanvas()

    pygame.display.update()

    frames.tick(fps)
