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

ancho, alto = 750, 350

ventana = pygame.display.set_mode( ( ancho , alto ) )

pygame.display.set_caption( 'Marcador para tenis de mesa' )

def mostrarEvento(evento):

    ventana.fill((0, 0, 0))
    fuente = pygame.font.SysFont(name, 200)
    imagenDeTexto = fuente.render(str(evento), True, (250, 250, 250))
    imagenDeTexto.blit(ventana, ( ( ancho / 2 - imagenDeTexto.get_rect(2) / 2 ) , ( alto / 2 - imagenDeTexto.get_rect(3) / 2 ) ) )


def salir():

    pygame.joystick.quit()
    pygame.font.quit()
    pygame.quit()
    sys.exit()

while True:

    for evento in eventos.get():

        if evento.type == JOYAXISMOTION :
            mostrarEvento(evento)
        
        if evento.type == JOYBALLMOTION :
            mostrarEvento(evento)
        
        if evento.type == JOYBUTTONDOWN :
            mostrarEvento(evento)
            
        if evento.type == JOYBUTTONUP : 
            mostrarEvento(evento)
            
        if evento.type == JOYHATMOTION :
            mostrarEvento(evento)

        if evento.type == JOYDEVICEADDED :
            mostrarEvento(evento)
            
        if evento.type == JOYDEVICEREMOVED:
            mostrarEvento(evento)

        if evento.type == KEYDOWN :
            mostrarEvento(evento)

        if evento.type == KEYUP :
            mostrarEvento(evento)

        if evento.type == globales.QUIT:
            salir()

    pygame.display.update()

    frames.tick(fps)