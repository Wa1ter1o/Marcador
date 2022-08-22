import pygame, sys, random
import time
import pygame.locals as globales
import pygame.event as eventos
import pygame.time as tiempo

pygame.init()
pygame.font.init()
pygame.mouse.set_visible(False)

frames = tiempo.Clock()
fps = 20
velocidadDeAnimacion = 10

ancho, alto = 1920, 1080
#obtener resolución de pantalla
infoPantalla = pygame.display.Info()
print(infoPantalla)
#eslaca de pantalla
escala = infoPantalla.current_w/ancho
print("escala: " + str(escala))
#escala = .83

ventana = pygame.display.set_mode((infoPantalla.current_h, infoPantalla.current_w),pygame.FULLSCREEN)

pygame.display.set_caption('Marcador para tenis de mesa')

fondo = pygame.image.load("assets/img/fondo.jpg")
fondo = pygame.transform.scale(fondo, (int(ancho * escala), int(alto * escala)))
print(logo.get_size())
logo = pygame.transform.scale(logo, (int(logo.get_size()[0]*escala), int(logo.get_size()[1]*escala)))

def dibujarFondo():
    print ("dibujando fondo")


while True:

    mover()
    dibujarFondo()
    dibujarHora()
    dibujarMarcos()


    for evento in eventos.get():

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                quit()

            if evento.key == pygame.K_LEFT:
                if elementos > 0:
                    marcosPorEliminar.append(marcos[0])
                    del(marcos[0])
                    elementos = len(marcos)
                    ajustarMedidas()
                    Ingresos.registrarIngreso((random.randint(1,11)))

            if evento.key == pygame.K_RIGHT:
                    marcos.append(Marco.Marco(pygame,ventana,elementos, elementos + 1, empleados[random.randint(0, 10)], escala))
                    elementos = len(marcos)
                    ajustarMedidas()
                    if elementos > 5:
                        marcosPorEliminar.append(marcos[0])
                        del (marcos[0])
                    Ingresos.registrarIngreso((random.randint(1, 11)))


        if evento.type == globales.QUIT:
            quit()


    pygame.display.update()

    frames.tick(fps)
