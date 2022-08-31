import math


class Jugador:

    def cambiarNombre(self, nombre):
        self.nombre = nombre

    def anotarPunto(self):
        self.puntos += 1

    def restarPunto(self):
        self.puntos -=1

    def anotarSet(self):
        self.sets +=1

    def restarSet(self):
        self.sets -= 1

    def reestablecerMarcadores(self):
        self.puntos = 0
        self.sets = 0

    def asignarfondo(self, fondo):
        self.fondo = fondo

    def generarImagen(self):
        iu = {
            "fuente": "OCR A Extended",
            "tFNombre": 100, "tFPuntos": 475, "tFSets": 250,
            "tFCNombre": (250, 250, 250), "tFCPuntos": ( 250, 250, 250 ), "tfCSets": (200, 200, 200),
            "yNombre": 75, "yPuntos": 150, "ySets": 600,
            "compSets": 225
        }

        imagen = self.pygame.Surface( ( 900, 900), self.pygame.SRCALPHA, 32 )
        imagen = imagen.convert_alpha()

        imagen.blit( self.fondo, ( 0, 0 ) )

        # Dibujado de nombre de jugador
        fuente = self.pygame.font.SysFont( iu["fuente"], int( iu["tFNombre"]  ) )
        imgTexto = fuente.render( self.nombre, True, iu["tFCNombre"] )
        imagen.blit( imgTexto, ( int( 900 / 2 - ( imgTexto.get_rect()[2]  ) / 2 ), iu["yNombre"] ) )

        # Dibujado de puntos
        fuente = self.pygame.font.SysFont(iu["fuente"], int(iu["tFPuntos"]))
        imgTexto = fuente.render(str( self.puntos ), True, iu["tFCPuntos"])
        imagen.blit(imgTexto, (int(900 / 2 - (imgTexto.get_rect()[2]) / 2), iu["yPuntos"]))

        # Dibujado de sets
        fuente = self.pygame.font.SysFont(iu["fuente"], int(iu["tFSets"]))
        imgTexto = fuente.render(str(self.sets), True, iu["tfCSets"])
        if self.lado == "izquierda":
            x = int( 900 / 2 - imgTexto.get_rect()[2]  / 2 + iu["compSets"])
        else:
            x = int(900 / 2 - imgTexto.get_rect()[2] / 2 - iu["compSets"])
        imagen.blit( imgTexto, ( x, iu["ySets"] ) )

        return imagen

    def cambiarLado(self):

        if self.lado == "izquierda":
            self.lado = "derecha"
            self.asignarPosLado()
        
        elif self.lado == "derecha":
            self.lado = "izquierda"
            self.asignarPosLado()

    def cambiarColor(self, fondo):

        self.fondo = fondo

    def mover(self, paso ):

        distMeta = abs( ( self.pos[0] - self.posFinal[0] ) )

        if distMeta > 0 and distMeta <= paso :
            self.pos[0] = self.posFinal[0]

        elif self.pos[0] < self.posFinal[0] :
            self.pos[0] += paso

        elif self.pos[0] > self.posFinal[0] :
            self.pos[0] -= paso

    def asignarPosLado(self):

        posIzquierda = [50, 120]
        posDerecha = [970, 120]

        if self.lado == "izquierda":
            self.posFinal = posIzquierda

        elif self.lado == "derecha":
            self.posFinal = posDerecha


    def __init__(self, pygame, nombre, saque, fondo, lado):

        self.pygame = pygame
        self.nombre = nombre
        self.puntos = 0
        self.sets = 0
        self.saque = saque
        self.fondo = fondo
        self.lado = lado

        self.posFinal = [ 0, 0 ]
        self.pos = [ 510, 50 ]

        self.asignarPosLado()

class pelota:

    def mover( self, paso ):

        distMeta = abs( ( self.pos[0] - self.posFinal[0] ) )

        if distMeta > 0 and distMeta <= paso * 2 :
            self.pos[0] = self.posFinal[0]

        elif self.pos[0] < self.posFinal[0] :
            self.pos[0] += paso * 1.5

        elif self.pos[0] > self.posFinal[0] :
            self.pos[0] -= paso * 1.5

        difCentro = abs( 960 - self.posFinal[0] )
        h = ( difCentro ** 2 - abs ( 960 - self.pos[0] ) ** 2 )

        if h > 0:
            h = h ** 0.5

        self.pos[1] = self.posFinal[1] - h / 2

    def cambiarLado(self):

        if self.lado == "izquierda":
            self.lado = "derecha"
            self.asignarPosLado()

        elif self.lado == "derecha":
            self.lado = "izquierda"
            self.asignarPosLado()

    def asignarPosLado(self):

        posIzquierda = [220, 780]
        posDerecha = [1700, 780]

        if self.lado == "izquierda":
            self.posFinal = posIzquierda

        elif self.lado == "derecha":
            self.posFinal = posDerecha

    def __init__(self, lado):

        self.lado = lado


        self.posFinal = [0, 780]
        self.pos = [0, 780]

        self.asignarPosLado()


