class Jugador:

    tamaño = [900, 900]
    posIzquierda = [60, 120]
    posDerecha = [910, 120]

    iu = { 
    "fuente" : "OCR A Extended", 
    "tFNombre" : 100, "tFMarcador" : 475, "tFSets" : 250, 
    "tFCNombre" : ( 250, 250, 250 ),
    "yNombre" : 75, "yMarcador" : 150, "ySets" : 500, 
    "compSets" : 300
    }

    def cambiarNombre(self, nombre):
        self.nombre = nombre

    def agregarPunto(self):
        self.puntos += 1

    def restarPunto(self):
        self.puntos -=1

    def agregarSet(self):
        self.sets +=1

    def restarSet(self):
        self.sets -= 1

    def reestablecerMarcadores(self):
        self.puntos = 0
        self.sets = 0

    def asignarfondo(self, fondo):
        self.fondo = fondo

    def generarImagen(self):

        imagen = self.pygame.Surface( tamaño )

        imagen.blit( self.fondo, ( 0, 0 ) )

    # Dibujado de nombre de jugador
    fuente = pygame.font.SysFont( iu["fuente"], int( iu["tFCNombre"]  ) )
    imgTexto = fuente.render( self.nombre, True, ( iu[txtNombreColor] ) )
    canvas.blit( imgTexto, 
        ( ( int( ( medidas["cuartoX"] - ( ( imgTexto.get_rect()[2]  ) / 2) + iu["compMarcos"] )  )), 
        ( int( iu["yNombre"]  ) ) ) )
    

    def cambiarLado(self):
        
        if self.lado == "izquierda":
            self.lado = "derecha"
            self.posFinal = posDerecha
        
        elif self.lado == "derecha":
            self.lado = "izquierda"
            self.posFinal = posIzquierda

    def cambiarColor(self, fondo):

        self.fondo = fondo

    def mover(self, paso ):

        distMeta = abs( ( self.pos[0] - self.posFinal ) )

        if distMeta > 0 and distMeta <= paso :
            self.pos[0] = self.posFinal[0]

        elif self.pos[0] < self.posFinal[0] :
            self.pos[0] += paso

        elif self.pos[0] > self.posFinal[0] :
            self.pos[0] -= paso
 


    def __init__(self, pygame, nombre, saque, fondo, lado):

        jugadorUno = { "puntos" : 0, "sets" : 0, "nombre" : "Jugador 1", "saque" : True, "color" : azul }

        self.pygame = pygame
        self.nombre = nombre
        self.puntos = 0
        self.sets = 0
        self.saque = saque
        self.fondo = fondo
        self.lado = lado

        self.posFinal = ( 0, 0 )
        self.pos = ( 0, 0 )

