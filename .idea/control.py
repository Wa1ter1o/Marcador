import pygame, sys, random
import pygame.locals as globales
import pygame.event as eventos
import pygame.time as tiempo
from pygame import joystick

pygame.init()

pygame.font.init()

frames = tiempo.Clock() 
fps = 30             

pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

ancho, alto = 1200, 250

ventana = pygame.display.set_mode( ( ancho , alto ) )

pygame.display.set_caption( 'Marcador para tenis de mesa' )

def mostrarEvento(evento):

    ventana.fill((0, 0, 0))
    fuente = pygame.font.SysFont('OCR A Extended', 20)
    imagenDeTexto = fuente.render(str(evento), True, (250, 250, 250))
    ventana.blit(imagenDeTexto, ( ( int (ancho / 2 - imagenDeTexto.get_rect()[2] / 2 ) ) , int( ( alto / 2 - imagenDeTexto.get_rect()[3] / 2 ) )) )
    #ventana.blit(imagenDeTexto, ( 10, 100 ) )
    print ( f'dibujado: {evento}')


def salir():

    pygame.joystick.quit()
    pygame.font.quit()
    pygame.quit()
    sys.exit()

while True:

    for evento in eventos.get():

        if evento.type == pygame.JOYAXISMOTION :
            mostrarEvento(evento)
        
        if evento.type == pygame.JOYBALLMOTION :
            mostrarEvento(evento)
        
        if evento.type == pygame.JOYBUTTONDOWN :
            mostrarEvento(evento)
            
        if evento.type == pygame.JOYBUTTONUP : 
            mostrarEvento(evento)
            
        if evento.type == pygame.JOYHATMOTION :
            mostrarEvento(evento)

        if evento.type == pygame.JOYDEVICEADDED :
            mostrarEvento(evento)
            
        if evento.type == pygame.JOYDEVICEREMOVED:
            mostrarEvento(evento)

        if evento.type == pygame.KEYDOWN :
            mostrarEvento(evento)

            if evento.key == pygame.K_ESCAPE:
                salir()

        if evento.type == pygame.KEYUP :
            mostrarEvento(evento)

        if evento.type == globales.QUIT:
            salir()

    pygame.display.update()

    frames.tick(fps)