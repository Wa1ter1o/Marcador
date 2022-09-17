import pygame, sys, random
from pathlib import Path
import pygame.locals as globales
import pygame.event as eventos
import pygame.time as tiempo
from pygame import mixer

import clases

pygame.init()
pygame.font.init()
pygame.mixer.init()
mixer.set_reserved(0)

mixer.music.fadeout(1)

#pygame.joystick.init()
#joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

pygame.mouse.set_visible(False)

frames = tiempo.Clock() 
fps = 30                            #velocidad de actualización en frames por segundo
velAnim = 1                         #tiempo en segundos para hacer cada animación
pasoAnim = 150                       #incremental de movimiento para todas las animaciones en pixels

milisegundos = tiempo.get_ticks()

ancho, alto = 1920, 1080
#obtener resolución de pantalla
infoPantalla = pygame.display.Info()
#print(infoPantalla)
#escala de pantalla
escala = infoPantalla.current_w / ancho
#print("escala: " + str(escala))
escala = 0.7  #Comentar para pantalla completa

ventana = pygame.display.set_mode( ( int( ancho * escala  ), int( alto * escala ) ) ) # Ventana 
#ventana = pygame.display.set_mode( ( int( ancho * escala  ), int( alto * escala ) ), pygame.FULLSCREEN ) #Pantalla completa

canvas = pygame.Surface( (ancho, alto) )

pygame.display.set_caption( 'Marcador para tenis de mesa' )

#-------------------------Cargando Imágenes y efectos de sonido--------------------------------------------------------------

fondoOriginal = pygame.image.load( "assets/img/fondo.jpg" )
fondo = pygame.transform.scale(fondoOriginal, ( int( ancho ) , int( alto  ) ) )

ganador = pygame.image.load( 'assets/img/ganador.jpg' )

azul = pygame.image.load( "assets/img/azul.jpg" )
rojo = pygame.image.load( "assets/img/rojo.jpg" )
color = True

volMusica = 10
volNarracion = 10
volEfectos = 10

musica = True
narracion = True
efectos = True

audiofx = {
    'bep' : mixer.Sound('assets/sonidos/fx/bep.wav') , 
    'bep2' : mixer.Sound('assets/sonidos/fx/bep2.wav'),
    'bep3' : mixer.Sound('assets/sonidos/fx/bep3.wav'),
    'bep4' : mixer.Sound('assets/sonidos/fx/bep4.wav'),
    'bep5' : mixer.Sound('assets/sonidos/fx/bep5.wav'),
    'punto' : mixer.Sound('assets/sonidos/fx/punto.wav'),
    'puntoMenos' : mixer.Sound('assets/sonidos/fx/puntoMenos.wav'),
    'set' : mixer.Sound('assets/sonidos/fx/set.wav') 
    }

rutas = list(Path('assets/sonidos/frases/Mariano/un punto').iterdir())
unPunto = []
for ruta in rutas:
    unPunto.append(mixer.Sound(str(ruta)))

rutas = list(Path('assets/sonidos/frases/Mariano/dos puntos').iterdir())
dosPuntos = []
for ruta in rutas:
    dosPuntos.append(mixer.Sound(str(ruta)))

rutas = list(Path('assets/sonidos/frases/Mariano/tres puntos').iterdir())
tresPuntos = []
for ruta in rutas:
    tresPuntos.append(mixer.Sound(str(ruta)))

rutas = list(Path('assets/sonidos/frases/Mariano/cuatro puntos').iterdir())
cuatroPuntos = []
for ruta in rutas:
    cuatroPuntos.append(mixer.Sound(str(ruta)))

rutas = list(Path('assets/sonidos/frases/Mariano/cinco puntos').iterdir())
cincoPuntos = []
for ruta in rutas:
    cincoPuntos.append(mixer.Sound(str(ruta)))

rutas = list(Path('assets/sonidos/frases/Mariano/seis puntos').iterdir())
seisPuntos = []
for ruta in rutas:
    seisPuntos.append(mixer.Sound(str(ruta)))

rutas = list(Path('assets/sonidos/frases/Mariano/siete puntos').iterdir())
sietePuntos = []
for ruta in rutas:
    sietePuntos.append(mixer.Sound(str(ruta)))

rutas = list(Path('assets/sonidos/frases/Mariano/dos puntos').iterdir())
DosPuntos = []
for ruta in rutas:
    DosPuntos.append(mixer.Sound(str(ruta)))

rutas = list(Path('assets/sonidos/frases/Mariano/dos puntos').iterdir())
DosPuntos = []
for ruta in rutas:
    DosPuntos.append(mixer.Sound(str(ruta)))

rutas = list(Path('assets/sonidos/frases/Mariano/dos puntos').iterdir())
DosPuntos = []
for ruta in rutas:
    DosPuntos.append(mixer.Sound(str(ruta)))

rutas = list(Path('assets/sonidos/frases/Mariano/ocho puntos').iterdir())
ochoPuntos = []
for ruta in rutas:
    ochoPuntos.append(mixer.Sound(str(ruta)))
rutas = list(Path('assets/sonidos/frases/Mariano/nueve puntos').iterdir())
nuevePuntos = []
for ruta in rutas:
    nuevePuntos.append(mixer.Sound(str(ruta)))

rutas = list(Path('assets/sonidos/frases/Mariano/diez puntos').iterdir())
diezPuntos = []
for ruta in rutas:
    diezPuntos.append(mixer.Sound(str(ruta)))
rutas = list(Path('assets/sonidos/frases/Mariano/mas diez puntos').iterdir())
masDiezPuntos = []
for ruta in rutas:
    masDiezPuntos.append(mixer.Sound(str(ruta)))


rutas = list(Path('assets/sonidos/frases/Mariano/felicidades').iterdir())
felicidades = []
for ruta in rutas:
    felicidades.append(mixer.Sound(str(ruta)))

rutas = list(Path('assets/sonidos/frases/Mariano/inicio de set').iterdir())
inicioSet = []
for ruta in rutas:
    inicioSet.append(mixer.Sound(str(ruta)))
rutas = list(Path('assets/sonidos/frases/Mariano/inicio de juego').iterdir())
inicioJuego = []
for ruta in rutas:
    inicioJuego.append(mixer.Sound(str(ruta)))
rutas = list(Path('assets/sonidos/frases/Mariano/gana set').iterdir())
ganaSet = []
for ruta in rutas:
    ganaSet.append(mixer.Sound(str(ruta)))

rutas = list(Path('assets/sonidos/frases/Mariano/gana juego').iterdir())
ganaJuego = []
for ruta in rutas:
    ganaJuego.append(mixer.Sound(str(ruta)))


carpetasMusicaFondo = list(Path('assets/sonidos/fondo').iterdir())
rutasMusica = []
nombreCarpetas = []
indiceMusicaFondo = 0

for carpeta in carpetasMusicaFondo:
    rutasMusica.append(list(Path(carpeta).iterdir()))
    cadena = str(carpeta)
    nombreInvertido = ''
    nombre = ''
    for letra in reversed(cadena):
        if letra == '\\' or letra == '/':
            break

        nombreInvertido = nombreInvertido + letra

    for letra in reversed(nombreInvertido):
        nombre = nombre + letra

    nombreCarpetas.append(nombre)

canalComentario = mixer.Channel(0)
reproducirComentario = []
reproducirEfecto = []
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& JUGADORES $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

jugadores = []
#jugadores.append({ "nombre" : "Adri" , "tts" : mixer.Sound('assets/sonidos/nombres/Adri.wav') } )
jugadores.append({ "nombre" : "Alejandro" , "tts" : mixer.Sound('assets/sonidos/nombres/Alejandro.wav') } )
jugadores.append({ "nombre" : "Alex" , "tts" : mixer.Sound('assets/sonidos/nombres/Alex.wav') } )
jugadores.append({ "nombre" : "Ami" , "tts" : mixer.Sound('assets/sonidos/nombres/Ami.wav') } )
#jugadores.append({ "nombre" : "Carlos" , "tts" : mixer.Sound('assets/sonidos/nombres/Carlos.wav') } )
jugadores.append({ "nombre" : "Cristian" , "tts" : mixer.Sound('assets/sonidos/nombres/Cristian.wav') } )
#jugadores.append({ "nombre" : "Daniela" , "tts" : mixer.Sound('assets/sonidos/nombres/Daniela.wav') } )
jugadores.append({ "nombre" : "Diego" , "tts" : mixer.Sound('assets/sonidos/nombres/Diego.wav') } )
jugadores.append({ "nombre" : "Emely" , "tts" : mixer.Sound('assets/sonidos/nombres/Emely.wav') } )
jugadores.append({ "nombre" : "Gladys" , "tts" : mixer.Sound('assets/sonidos/nombres/Gladys.wav') } )
jugadores.append({ "nombre" : "Ivon" , "tts" : mixer.Sound('assets/sonidos/nombres/Ivon.wav') } )
jugadores.append({ "nombre" : "Javi" , "tts" : mixer.Sound('assets/sonidos/nombres/Javi.wav') } )
#jugadores.append({ "nombre" : "Jorge" , "tts" : mixer.Sound('assets/sonidos/nombres/Jorge.wav') } )
#jugadores.append({ "nombre" : "José" , "tts" : mixer.Sound('assets/sonidos/nombres/Jose.wav') } )
#jugadores.append({ "nombre" : "Josue" , "tts" : mixer.Sound('assets/sonidos/nombres/Josue.wav') } )
jugadores.append({ "nombre" : "Jugador Uno" , "tts" : mixer.Sound('assets/sonidos/nombres/Jugador uno.wav') } )
jugadores.append({ "nombre" : "Jugador Dos" , "tts" : mixer.Sound('assets/sonidos/nombres/Jugador dos.wav') } )
jugadores.append({ "nombre" : "Lilly" , "tts" : mixer.Sound('assets/sonidos/nombres/Lilly.wav') } )
#jugadores.append({ "nombre" : "Luis" , "tts" : mixer.Sound('assets/sonidos/nombres/Luis.wav') } )
#jugadores.append({ "nombre" : "Mario" , "tts" : mixer.Sound('assets/sonidos/nombres/Mario.wav') } )
jugadores.append({ "nombre" : "Pablo" , "tts" : mixer.Sound('assets/sonidos/nombres/Pablo.wav') } )
jugadores.append({ "nombre" : "Paco" , "tts" : mixer.Sound('assets/sonidos/nombres/Paco.wav') } )
jugadores.append({ "nombre" : "Sebas" , "tts" : mixer.Sound('assets/sonidos/nombres/Sebas.wav') } )
jugadores.append({ "nombre" : "Titi" , "tts" : mixer.Sound('assets/sonidos/nombres/Titi.wav') } )
#jugadores.append({ "nombre" : "Tito" , "tts" : mixer.Sound('assets/sonidos/nombres/Tito.wav') } )
#jugadores.append({ "nombre" : "Vale" , "tts" : mixer.Sound('assets/sonidos/nombres/Vale.wav') } )
jugadores.append({ "nombre" : "Walter" , "tts" : mixer.Sound('assets/sonidos/nombres/Walter.wav') }) 
jugadores.append({ "nombre" : "William" , "tts" : mixer.Sound('assets/sonidos/nombres/William.wav') })
jugadores.append({ "nombre" : "Willy" , "tts" : mixer.Sound('assets/sonidos/nombres/Willy.wav') } )

     
nombres = []
for jugador in jugadores:
    nombres.append(jugador['nombre'])

#*****************************VARIABLES DEL JUEGO****************************************************************************

iu = { 'fuente' : 'OCR A Extended' }

jugadorUno = clases.Jugador(pygame, "Jugador Uno", mixer.Sound('assets/sonidos/nombres/Jugador uno.wav'),True, azul, "izquierda")
jugadorDos = clases.Jugador(pygame, "Jugador Dos", mixer.Sound('assets/sonidos/nombres/Jugador dos.wav') ,False, rojo, "derecha")

pelota = clases.pelota( "izquierda" )


sets = 1    
nSet = 0                        #sets a jugar
puntosPorSet = 11               #puntos a jugar por set
cambioSaque = 2                 #número de saques para hacer cambio de saque
lado = True                     #define de que lado se encuentra cada jugador
saque = True                    #si es True el saque le corresponde al jugador uno
primerSaque = 'izquierda'

milisUltimoPunto = 0
milisProteccionPunto = 1000


puntosTotalesSet = 0
anotaciones = []
datosSets = [ [" " , " "] , [" " , " "] , [" ", " "] , [" " , " "] , [" " , " "] ]

#              0             1            2          3               4             5          6          7
estados = ( "inicio" , "post juego" , "cuenta",  "jugando" , "post nuevo set" , "pausa" , "post fin" , "fin" )

estado = estados[ 0 ]

tPres = { "1" : False , "esc" : False , "jIzquierda" : False , 'jDerecha' : False , 'j0' : False}

botones = False
arbitro = False

segInicioCuentaRegresiva = None
contandoSegudos = False

beeps = [ 0, 0, 0, 0 ]

#////////////////////////////// LISTAS DE MENÚ //////////////////////////////////////////////////////////////////////////////

indicesMenu = { 'inicio' : 0 , 'pausa' : 0, 'fin' : 0, 'post nuevo set' : 0 }

datosInicio = [
    {
        'titulo' : 'Jugador 1', 'dato' : jugadorUno.nombre, 'datos' : nombres, 'indice' : 0
    },
    {
        'titulo' : 'Jugador 2', 'dato' : jugadorDos.nombre, 'datos' : nombres, 'indice' : 0
    },
    {
        'titulo' : 'Sets' , 'dato' : sets
    },
    {
        'titulo' : 'Pts. Por Set' , 'dato' : puntosPorSet
    },
    {
        'titulo' : 'Saque Inicial' , 'dato' : jugadorUno.nombre, 'datos' : [ jugadorUno.nombre, jugadorDos.nombre, 'Sorteo'], 'indice' : 0
    }

]

menuInicio = clases.menu(pygame, 'INICIO', 'Espacio Para Continuar', datosInicio, indicesMenu['inicio'] )

datosPausa = [
    {
        'titulo' : 'Vol de música' , 'dato' : volMusica
    },
    {
        'titulo' : 'vol de voz' , 'dato' : volNarracion
    },
    {
        'titulo' : 'vol efectos' , 'dato' : volEfectos
    },
    {
        'titulo' : 'Música' , 'dato' : nombreCarpetas[indiceMusicaFondo]
    },
    {
        'titulo' : 'Nuevo Juego' , 'dato' : 'No'
    }
    

]

menuPausa = clases.menu(pygame, 'PAUSA', 'Espacio Para Continuar', datosPausa, indicesMenu['pausa'] )


datosFin = [
    {
        'titulo' : jugadorUno.nombre , 'dato' : jugadorDos.nombre
    },
    {
        'titulo' : datosSets[0][0] , 'dato' : datosSets[0][1]
    },
    {
        'titulo' : datosSets[1][0] , 'dato' : datosSets[1][1]
    },
    {
        'titulo' : datosSets[2][0] , 'dato' : datosSets[2][1]
    },
    {
        'titulo' : datosSets[3][0] , 'dato' : datosSets[3][1]
    },
    {
        'titulo' : datosSets[4][0] , 'dato' : datosSets[4][1]
    },
 
]

menuFin = clases.menu(pygame, 'FIN DEL JUEGO', 'Espacio Para Comenzar de Nuevo', datosFin, indicesMenu['fin'] )

datosPostNuevoSet = [
    {
        'titulo' : jugadorUno.nombre , 'dato' : jugadorDos.nombre
    },
    {
        'titulo' : ' ' , 'dato' : ' '
    },
    {
        'titulo' : jugadorUno.puntos, 'dato' : jugadorDos.puntos
    }
]

menuPostNuevoSet = clases.menu(pygame, 'FIN DEL SET', 'ESPACIO: continuar, BACKSPACE: cancelar', datosPostNuevoSet, indicesMenu['post nuevo set'])

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

    elif estado == estados[ 2 ] :
        cuentaRegresiva()

    elif estado == estados[5] :
        canvas.blit( menuPausa.generarImagen(), menuPausa.pos)

    elif estado == estados[4] :
        canvas.blit( menuPostNuevoSet.generarImagen(), menuPostNuevoSet.pos)

    elif estado == estados[7]: # Fin del juego
        canvas.blit( menuFin.generarImagen(), menuFin.pos)

        if jugadorUno.sets >= jugadorDos.sets and jugadorUno.sets > 0:
            canvas.blit(ganador, ( ( ancho / 4 - ( ganador.get_rect()[2] ) / 2), alto / 2 - 50 - ( ganador.get_rect()[3] ) / 2 ) )
        if jugadorDos.sets >= jugadorUno.sets and jugadorDos.sets > 0:
            canvas.blit(ganador, ( ( ancho / 4 * 3 - ( ganador.get_rect()[2] ) / 2), alto / 2 - 50 - ( ganador.get_rect()[3] ) / 2 ) )

        fuente = pygame.font.SysFont( iu["fuente"], 300 ) 
        imgTexto = fuente.render(str( jugadorUno.sets ), True, ( 255, 145, 53 ) )
        canvas.blit(imgTexto, ( ( ancho / 4 - ( imgTexto.get_rect()[2] ) / 2), alto / 3 * 2 + 25 - ( imgTexto.get_rect()[3] ) / 2 ) ) 

        imgTexto = fuente.render(str( jugadorDos.sets ), True, ( 255, 145, 53 ) )
        canvas.blit(imgTexto, ( ( ancho / 4 * 3 - ( imgTexto.get_rect()[2] ) / 2), alto / 3 * 2 + 25 - ( imgTexto.get_rect()[3] ) / 2 ) ) 

def dibujarPuntero(puntero, lado) :

    if lado == 'izquierda' :
        fuente = pygame.font.SysFont( iu["fuente"], 300 ) 
        imgTexto = fuente.render( puntero , True, ( 16, 255, 13 ) )
        canvas.blit(imgTexto, ( ( ancho / 4 - ( imgTexto.get_rect()[2] ) / 2), alto / 3 * 2 + 25 - ( imgTexto.get_rect()[3] ) / 2 ) )

    elif lado == 'derecha' :
        fuente = pygame.font.SysFont( iu["fuente"], 300 ) 
        imgTexto = fuente.render( puntero , True, ( 16, 255, 13 ) )
        canvas.blit(imgTexto, ( ( ancho - ancho / 4 - ( imgTexto.get_rect()[2] ) / 2), alto / 3 * 2 + 25 - ( imgTexto.get_rect()[3] ) / 2 ) )

def tocarMusica() :

    if musica :
        mixer.music.stop()
        mixer.music.load(str(rutasMusica[indiceMusicaFondo][random.randint(0, len(rutasMusica[indiceMusicaFondo]) - 1)]))
        mixer.music.play(-1)

def pausarMusica() :

    mixer.music.pause()

def seguirMusica():

    if musica :
        mixer.music.unpause()

def setearVolumen(vol):

    mixer.music.set_volume(vol / 10)


def reproducirCola():
    global reproducirComentario, reproducirEfecto

    if len(reproducirComentario) > 0 and not canalComentario.get_busy():
        audio = reproducirComentario.pop(0)
        audio.set_volume( volNarracion / 10 )
        audio.play(0)
        setearVolumen(volMusica / 4)
    
    if len(reproducirComentario) == 0 and not canalComentario.get_busy():
        setearVolumen(volMusica)

    if len(reproducirEfecto) > 0 :
        audio = reproducirEfecto.pop(0)
        audio.set_volume( volEfectos / 10 )
        audio.play()


def cuentaRegresiva():
    global segInicioCuentaRegresiva, contandoSegudos, estado, beeps, nSet, primerSaque

    if not contandoSegudos :
        segInicioCuentaRegresiva = milisegundos / 1000
        contandoSegudos = True


    segFaltantes =  3.8 - (milisegundos / 1000 - segInicioCuentaRegresiva )
    
    fuente = pygame.font.SysFont( iu["fuente"], 1080 ) 
    imgTexto = fuente.render(str( int ( segFaltantes ) ), True, ( 255, 145, 53 ) )
    canvas.blit(imgTexto, ( ( ancho / 2 - ( imgTexto.get_rect()[2] ) / 2), alto / 2 - ( imgTexto.get_rect()[3] ) / 2 ) ) 

    if segFaltantes < 4 and beeps[0] == 0 :
        audiofx['bep'].set_volume(volEfectos)
        audiofx['bep'].play()
        if nSet == 0 and datosInicio[4]['indice'] == 2:
            if random.randint(0, 1) == 1:
                cambiarSaque()
        beeps[0] = 1
        
    if segFaltantes < 3 and beeps[1] == 0 :
        audiofx['bep'].set_volume(volEfectos)
        audiofx['bep'].play()
        if nSet == 0 and datosInicio[4]['indice'] == 2:
            if random.randint(0, 1) == 1:
                cambiarSaque()
        beeps[1] = 1

    if segFaltantes < 2 and beeps[2] == 0 :
        audiofx['bep'].set_volume(volEfectos)
        audiofx['bep'].play()
        if nSet == 0 and datosInicio[4]['indice'] == 2:
            if random.randint(0, 1) == 1:
                cambiarSaque()
        beeps[2] = 1

    if segFaltantes < 1 and beeps[3] == 0 :
        audiofx['bep2'].set_volume(volEfectos)
        audiofx['bep2'].play()
        if nSet == 0 and datosInicio[4]['indice'] == 2:
            if random.randint(0, 1) == 1:
                cambiarSaque()
        beeps[3] = 1
    
    if segFaltantes < 0.2 : 
        estado = estados[3]
        contandoSegudos = False
        beeps = [ 0, 0, 0, 0]

        setearVolumen(volMusica)
        if nSet == 0:
            tocarMusica()
            reproducirComentario.append( inicioJuego[ random.randint( 0, len(inicioJuego) - 1 ) ] )
        else:
            tocarMusica()

        nSet += 1
        reproducirComentario.append( inicioSet[ random.randint( 0, len(inicioSet) - 1 ) ] )

        if nSet == 1:
            if jugadorUno.saque :
                primerSaque = jugadorUno.lado

            elif jugadorDos.saque:
                primerSaque = jugadorDos.lado


def comprobarReglas():
    global estado, reproducirComentario

    if ( puntosPorSet - jugadorUno.puntos <= 1 ) and ( puntosPorSet - jugadorDos.puntos <= 1 ) :
        cambiarSaque()
    elif puntosTotalesSet % cambioSaque == 0:
        cambiarSaque()

    pInvParaGanar = ( puntosPorSet + 3 ) / 2 
    if ( jugadorUno.puntos == pInvParaGanar or jugadorDos.puntos == pInvParaGanar) and \
        ( jugadorUno.puntos == 0 or jugadorDos.puntos == 0 ) :
        audiofx['set'].set_volume( volEfectos / 10 )
        reproducirEfecto.append(audiofx['set'])
        pasarDatosSet()
        estado = estados[4] # Pre Nuevo Set
        pausarMusica()
        reproducirComentario = []
        if jugadorUno.puntos > jugadorDos.puntos:
            reproducirComentario.append(jugadorUno.tts)
        else:
            reproducirComentario.append(jugadorDos.tts)
        reproducirComentario.append( ganaSet[random.randint(0, len(ganaSet) - 1)] )

    if ( (jugadorUno.puntos >= puntosPorSet ) or ( jugadorDos.puntos >= puntosPorSet ) ) \
        and abs( jugadorUno.puntos - jugadorDos.puntos ) >= 2 :
        audiofx['set'].set_volume( volEfectos / 10 )
        reproducirEfecto.append(audiofx['set'])
        pasarDatosSet()
        estado = estados[4] # Pre Nuevo Set
        pausarMusica()
        reproducirComentario = []
        if jugadorUno.puntos > jugadorDos.puntos:
            reproducirComentario.append(jugadorUno.tts)
        else:
            reproducirComentario.append(jugadorDos.tts)
        reproducirComentario.append( ganaSet[random.randint(0, len(ganaSet) - 1)] )

    #print(estado)

def agregarComentario(clave, puntos):
    global reproducirComentario

    if clave == 'punto':
        if puntos == 1:
            reproducirComentario.append(unPunto[random.randint(0, len(unPunto) - 1 ) ] )
        elif puntos == 2:
            reproducirComentario.append(dosPuntos[random.randint(0, len(dosPuntos) - 1 ) ] )
        elif puntos == 3:
            reproducirComentario.append(tresPuntos[random.randint(0, len(tresPuntos) - 1 ) ] )
        elif puntos == 4:
            reproducirComentario.append(cuatroPuntos[random.randint(0, len(cuatroPuntos) - 1 ) ] )
        elif puntos == 5:
            reproducirComentario.append(cincoPuntos[random.randint(0, len(cincoPuntos) - 1 ) ] )
        elif puntos == 6:
            reproducirComentario.append(seisPuntos[random.randint(0, len(seisPuntos) - 1 ) ] )
        elif puntos == 7:
            reproducirComentario.append(sietePuntos[random.randint(0, len(sietePuntos) - 1 ) ] )
        elif puntos == 8:
            reproducirComentario.append(ochoPuntos[random.randint(0, len(ochoPuntos) - 1 ) ] )
        elif puntos == 9:
            reproducirComentario.append(nuevePuntos[random.randint(0, len(nuevePuntos) - 1 ) ] )
        elif puntos == 10:
            reproducirComentario.append(diezPuntos[random.randint(0, len(diezPuntos) - 1 ) ] )
        elif puntos > 10:
            reproducirComentario.append(masDiezPuntos[random.randint(0, len(masDiezPuntos) - 1 ) ] )


def anotarPunto(jugador):
    global puntosTotalesSet, milisUltimoPunto

    if milisProteccionPunto < milisegundos - milisUltimoPunto :

        milisUltimoPunto = milisegundos

        if jugador == 1:
            jugadorUno.anotarPunto()
            anotaciones.append(1)
            jugadorUno.puntosSeguidos += 1
            jugadorDos.puntosSeguidos = 0
            if narracion :
                reproducirComentario.append(jugadorUno.tts)
                agregarComentario('punto', jugadorUno.puntosSeguidos)

        if jugador == 2:
            jugadorDos.anotarPunto()
            anotaciones.append(2)
            jugadorDos.puntosSeguidos += 1
            jugadorUno.puntosSeguidos = 0
            if narracion :
                reproducirComentario.append(jugadorDos.tts)
                agregarComentario('punto', jugadorDos.puntosSeguidos)

        puntosTotalesSet += 1

        audiofx['punto'].set_volume( volEfectos / 10 )
        audiofx['punto'].play()

        if nSet <= 5 :
            datosSets[nSet - 1][0] = jugadorUno.puntos
            datosSets[nSet - 1][1] = jugadorDos.puntos

        comprobarReglas()

def retrocederPunto():
    global anotaciones, puntosTotalesSet, estado

    if len(anotaciones) > 0 :

        anotacion = anotaciones.pop()
        
        if anotacion == 1 :
            jugadorUno.puntos -= 1
            jugadorUno.puntosSeguidos -= 1
        elif anotacion == 2 : 
            jugadorDos.puntos -= 1
            jugadorDos.puntosSeguidos -=1

        puntosTotalesSet -= 1

        if puntosTotalesSet % 2:
            cambiarSaque()

        if estado == estados[4] :
            estado = estados[3]
            seguirMusica()

        audiofx['puntoMenos'].play()




def anotarSet():

    if jugadorUno.puntos > jugadorDos.puntos :
        jugadorUno.anotarSet()

    elif jugadorDos.puntos > jugadorUno.puntos :
        jugadorDos.anotarSet()

    iniciarPuntos()
    
    

def iniciarMarcadores():
    global puntosTotalesSet, datosSets, nSet

    jugadorUno.puntos = 0
    jugadorUno.puntosSeguidos = 0
    jugadorUno.sets = 0

    jugadorDos.puntos = 0
    jugadorDos.puntosSeguidos = 0
    jugadorDos.sets = 0

    puntosTotalesSet = 0

    nSet = 0

    datosSets = [ [" " , " "] , [" " , " "] , [" ", " "] , [" " , " "] , [" " , " "] ]

    if datosInicio[4]['dato'] == jugadorUno.nombre :
        if jugadorDos.saque :
            cambiarSaque()
    elif datosInicio[4]['dato'] == jugadorDos.nombre:
        if jugadorUno.saque : 
            cambiarSaque()

    if jugadorUno.lado == 'derecha' :
        cambiarLado()

def pasarDatosSets(): #Le transfiere los datos de datosSets a datosFin 
    global datosFin

    datosFin[0]['titulo'] = jugadorUno.nombre
    datosFin[0]['dato'] = jugadorDos.nombre

    for i, dato in enumerate(datosSets) :
        #print ( i , " ",  dato )
        if i > 5 :
            break
        datosFin[i+1]['titulo'] = dato[0]
        datosFin[i+1]['dato'] = dato[1]

def pasarDatosSet() : # Transfiere datos del set acutal a datosPostNuevoSet
    global datosPostNuevoSet

    datosPostNuevoSet[0]['titulo'] = jugadorUno.nombre
    datosPostNuevoSet[0]['dato'] = jugadorDos.nombre

    datosPostNuevoSet[2]['titulo'] = jugadorUno.puntos
    datosPostNuevoSet[2]['dato'] = jugadorDos.puntos

def iniciarPuntos():
    global puntosTotalesSet, anotaciones

    jugadorUno.puntos = 0
    jugadorUno.puntosSeguidos = 0

    jugadorDos.puntos = 0
    jugadorDos.puntosSeguidos = 0

    puntosTotalesSet = 0

    anotaciones = [] 


def cambiarLado():
    global lado

    jugadorUno.cambiarLado()
    jugadorDos.cambiarLado()

    pelota.cambiarLado()
    lado = not lado

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

def procesarDerecha():
    global sets, puntosPorSet, volMusica, volNarracion, volEfectos, musica, narracion, efectos, indiceMusicaFondo

    #Manejando menú inicio
    if estado == estados[0]:

        #Jugador Uno
        if indicesMenu['inicio'] == 0:

            if datosInicio[0]['indice'] < len(datosInicio[0]['datos']) - 1 :

                datosInicio[0]['indice'] += 1

            else:

                datosInicio[0]['indice'] = 0

            jugadorUno.nombre = jugadores[datosInicio[0]['indice']]['nombre']
            jugadorUno.tts = jugadores[datosInicio[0]['indice']]['tts']
            jugadorUno.tts.set_volume(volNarracion / 10)
            jugadorUno.tts.play()
            datosInicio[0]['dato'] = jugadorUno.nombre
            datosInicio[4]['datos'][0] = jugadorUno.nombre  # Para menú de saque inicial
            datosInicio[4]['dato'] = datosInicio[4]['datos'][datosInicio[4]['indice']]  # Para menú de saque inicial

        #Jugador dos
        elif indicesMenu['inicio'] == 1:

            if datosInicio[1]['indice'] < len(datosInicio[1]['datos']) - 1 :

                datosInicio[1]['indice'] += 1

            else:

                datosInicio[1]['indice'] = 0

            jugadorDos.nombre = jugadores[datosInicio[1]['indice']]['nombre']
            jugadorDos.tts = jugadores[datosInicio[1]['indice']]['tts']
            jugadorDos.tts.set_volume(volNarracion / 10)
            jugadorDos.tts.play()
            datosInicio[1]['dato'] = jugadorDos.nombre
            datosInicio[4]['datos'][1] = jugadorDos.nombre # Para menú de inicio, saque incial
            datosInicio[4]['dato'] = datosInicio[4]['datos'][datosInicio[4]['indice']]  # Para menú de inicio, saque inicial

        # Sets del juego
        elif indicesMenu['inicio'] == 2:
            
            if sets < 21:
                sets += 2   
                datosInicio[2]['dato'] = sets

        # Puntos por juego
        elif indicesMenu['inicio'] == 3:
            
            if puntosPorSet < 21:
                puntosPorSet += 2
                datosInicio[3]['dato'] = puntosPorSet

        # Saque inicial
        elif indicesMenu['inicio'] == 4:
            
            if datosInicio[4]['indice'] < len(datosInicio[4]['datos']) - 1 :

                datosInicio[4]['indice'] += 1

            else:

                datosInicio[4]['indice'] = 0

            datosInicio[4]['dato'] = datosInicio[4]['datos'][datosInicio[4]['indice']] 

            if datosInicio[4]['dato'] == jugadorUno.nombre:  
                
                if  not jugadorUno.saque :
                    cambiarSaque()

            elif datosInicio[4]['dato'] == jugadorDos.nombre:  
                
                if  not jugadorDos.saque :
                    cambiarSaque()

    elif estado == estados[5]: # pausa
        
        if indicesMenu['pausa'] == 0 : #Volumen de Música
            if volMusica < 10 :
                volMusica += 1
                datosPausa[0]['dato'] = volMusica
            musica = True
            setearVolumen(volMusica)

        elif indicesMenu['pausa'] == 1 : #Volumen de Narración
            if volNarracion < 10 :
                volNarracion += 1
                datosPausa[1]['dato'] = volNarracion
            narracion = True

        elif indicesMenu['pausa'] == 2 : #Volumen de efectos
            if volEfectos < 10 :
                volEfectos += 1
                datosPausa[2]['dato'] = volEfectos
            efectos = True

        elif indicesMenu['pausa'] == 3 : #Musica
            if indiceMusicaFondo < len(carpetasMusicaFondo) - 1 :
                indiceMusicaFondo += 1
            else:
                indiceMusicaFondo = 0
            datosPausa[3]['dato'] = nombreCarpetas[indiceMusicaFondo]
            tocarMusica()
            pausarMusica()

        elif indicesMenu['pausa'] == 4 : # Nuevo juego
            if datosPausa[4]['dato'] == 'No':
                datosPausa[4]['dato'] = 'Si'
            else:
                datosPausa[4]['dato'] = 'No'

    audiofx['bep3'].set_volume(volEfectos)
    audiofx['bep3'].play()

def procesarIzquierda():
    global sets, puntosPorSet, volMusica, volNarracion, volEfectos, musica, narracion, efectos, indiceMusicaFondo

    if estado == estados[0]: # Inicio

        #Jugador uno
        if indicesMenu['inicio'] == 0:

            if datosInicio[0]['indice'] > 0 :

                datosInicio[0]['indice'] -= 1

            else:

                datosInicio[0]['indice'] = len(datosInicio[0]['datos']) - 1

            jugadorUno.nombre = jugadores[datosInicio[0]['indice']]['nombre']
            jugadorUno.tts = jugadores[datosInicio[0]['indice']]['tts']
            jugadorUno.tts.set_volume(volNarracion / 10)
            jugadorUno.tts.play()
            datosInicio[0]['dato'] = jugadorUno.nombre
            datosInicio[4]['datos'][0] = jugadorUno.nombre #Asignación de dato para cambio de saque
            datosInicio[4]['dato'] = datosInicio[4]['datos'][datosInicio[4]['indice']]  # Para menú de inicio, saque inicial



        #jugador Dos
        elif indicesMenu['inicio'] == 1:

            if datosInicio[1]['indice'] > 0 :

                datosInicio[1]['indice'] -= 1
                
            else:

                datosInicio[1]['indice'] = len(datosInicio[1]['datos']) - 1

            jugadorDos.nombre = jugadores[datosInicio[1]['indice']]['nombre']
            jugadorDos.tts = jugadores[datosInicio[1]['indice']]['tts']
            jugadorDos.tts.set_volume(volNarracion / 10)
            jugadorDos.tts.play()
            datosInicio[1]['dato'] = jugadorDos.nombre
            datosInicio[4]['datos'][1] = jugadorDos.nombre #Asignación de dato para cambio de saque
            datosInicio[4]['dato'] = datosInicio[4]['datos'][datosInicio[4]['indice']]  # Para menú de inicio, saque inicial


        #Sets
        elif indicesMenu['inicio'] == 2:
            
            if sets > 1:
                sets -= 2
                datosInicio[2]['dato'] = sets

        #Puntos por set
        elif indicesMenu['inicio'] == 3:
            
            if puntosPorSet > 7:
                puntosPorSet -= 2
                datosInicio[3]['dato'] = puntosPorSet

        #saque inicial
        elif indicesMenu['inicio'] == 4:
            
            if datosInicio[4]['indice'] > 0 :

                datosInicio[4]['indice'] -= 1

            else:

                datosInicio[4]['indice'] = len(datosInicio[4]['datos']) - 1

            datosInicio[4]['dato'] = datosInicio[4]['datos'][datosInicio[4]['indice']] 

            if datosInicio[4]['dato'] == jugadorUno.nombre:  
                
                if  not jugadorUno.saque :
                    cambiarSaque()

            elif datosInicio[4]['dato'] == jugadorDos.nombre:  
                
                if  not jugadorDos.saque :
                    cambiarSaque()

    elif estado == estados[5]: # Pausa

        if indicesMenu['pausa'] == 0 : #Volumen de música

            if volMusica > 0 :
                volMusica -= 1
                datosPausa[0]['dato'] = volMusica
                if volMusica == 0 :
                    musica == False

            setearVolumen(volMusica)

        elif indicesMenu['pausa'] == 1 : #Volumen de narracion

            if volNarracion > 0 :
                volNarracion -= 1
                datosPausa[1]['dato'] = volNarracion
                if volNarracion == 0 :
                    narracion == False

        elif indicesMenu['pausa'] == 2 : #Volumen de efectos

            if volEfectos > 0 :
                volEfectos -= 1
                datosPausa[2]['dato'] = volEfectos
                if volEfectos == 0 :
                    efectos == False

        elif indicesMenu['pausa'] == 3 : #Musica
            if indiceMusicaFondo > 0 :
                indiceMusicaFondo -= 1
            else:
                indiceMusicaFondo = len(carpetasMusicaFondo) - 1
            datosPausa[3]['dato'] = nombreCarpetas[indiceMusicaFondo]
            tocarMusica()
            pausarMusica()

        elif indicesMenu['pausa'] == 4 : # Nuevo juego
            if datosPausa[4]['dato'] == 'No':
                datosPausa[4]['dato'] = 'Si'
            else:
                datosPausa[4]['dato'] = 'No'

    audiofx['bep3'].set_volume(volEfectos)
    audiofx['bep3'].play()

def procesarAbajo():

    if estado == estados[0]: # Inicio

        if indicesMenu['inicio'] < len(datosInicio) - 1:

            indicesMenu['inicio'] += 1

        else:
            indicesMenu['inicio'] = 0

        menuInicio.indice = indicesMenu['inicio']

    if estado == estados[5]: # Pausa

        if indicesMenu['pausa'] < len(datosPausa) - 1:

            indicesMenu['pausa'] += 1

        else:
            indicesMenu['pausa'] = 0

        menuPausa.indice = indicesMenu['pausa']

    audiofx['bep4'].set_volume(volEfectos)
    audiofx['bep4'].play()

def procesarArriba():

    if estado == estados[0]:

        if indicesMenu['inicio'] > 0 :

            indicesMenu['inicio'] -= 1

        else:
            indicesMenu['inicio'] = len(datosInicio) - 1

        menuInicio.indice = indicesMenu['inicio']

    if estado == estados[5]: # Pausa

        if indicesMenu['pausa'] > 0:

            indicesMenu['pausa'] -= 1

        else:
            indicesMenu['pausa'] = len(datosPausa) - 1

        menuPausa.indice = indicesMenu['pausa']

    audiofx['bep4'].set_volume(volEfectos)
    audiofx['bep4'].play()

def procesarContinuar():
    global estado, reproducirComentario

#                0             1            2          3              4              5           6         7
# estados = ( "inicio" , "post juego" , "cuenta",  "jugando" , "post nuevo set" , "pausa" , "post fin" , "fin" )

    if estado == estados[0]:    # Inicio
        estado = estados[2]     # Post juego
        reproducirComentario = []

    elif estado == estados[1]:  # Post juego
        estado = estados[2]     # cuenta

    elif estado == estados[3]:  # jugando
        estado = estados[5]     # pausa
        pausarMusica()

    elif estado == estados[5] and datosPausa[4]['dato'] == 'Si': # Nuevo Juego
        pasarDatosSets()
        estado = estados[7]
        datosPausa[4]['dato'] = 'No'
        reproducirComentario = []

        if jugadorUno.sets > jugadorDos.sets:
            reproducirComentario.append( felicidades[random.randint(0, len(felicidades) - 1)] )
            reproducirComentario.append(jugadorUno.tts)
            reproducirComentario.append( ganaJuego[random.randint(0, len(ganaJuego) - 1)] )
        if jugadorDos.sets > jugadorUno.sets:
            reproducirComentario.append( felicidades[random.randint(0, len(felicidades) - 1)] )
            reproducirComentario.append(jugadorDos.tts)
            reproducirComentario.append( ganaJuego[random.randint(0, len(ganaJuego) - 1)] )

    elif estado == estados[5]:  # pausa
        estado = estados[3]     # jugando
        seguirMusica()
    
    elif estado == estados[4]:  # post nuevo set
        anotarSet()
        if jugadorUno.sets > sets / 2 or jugadorDos.sets > sets / 2 : # si alguno ganó más de la mitad de sets
            pasarDatosSets()
            estado = estados[7]
            reproducirComentario = []

            reproducirComentario.append( felicidades[random.randint(0, len(felicidades) - 1)] )
            if jugadorUno.sets > jugadorDos.sets:
                reproducirComentario.append(jugadorUno.tts)
            if jugadorDos.sets > jugadorUno.sets:
                reproducirComentario.append(jugadorDos.tts)
            reproducirComentario.append( ganaJuego[random.randint(0, len(ganaJuego) - 1)] )

        else:
            
            cambiarLado()

            if jugadorUno.saque : 
                if not (jugadorUno.lado == primerSaque) :
                    cambiarSaque() 
            elif jugadorDos.saque:
                if not(jugadorDos.lado == primerSaque) :
                    cambiarSaque()


            
            estado = estados[2]     # cuenta

    elif estado == estados[7]:  # fin
        estado = estados[0]     # inicio
        iniciarMarcadores()

    audiofx['bep5'].set_volume(volEfectos)
    audiofx['bep5'].play()

def procesarPuntoIzquierda():

    # si estado es jugando
    if estado == estados[3] :
        if lado :
            anotarPunto(1)
        else:
            anotarPunto(2)

def procesarPuntoDerecha():

    # si estado es jugando
    if estado == estados[3] :
        if lado :
            anotarPunto(2)
        else:
            anotarPunto(1)

def quit():
    #pygame.joystick.quit()   # Quitar comentario si se usa con joystick
    pygame.mixer.quit()
    pygame.font.quit()
    pygame.quit()
    sys.exit()

#----------------------------------CICLO PRINCIPAL---------------------------------------------------------------------------    

setearVolumen(volMusica)
dibujarFondo()


while True:

    milisegundos = tiempo.get_ticks()
    mover()

    if estado == estados[2] or estado == estados[3] :

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
                procesarIzquierda()

            if evento.key == pygame.K_RIGHT:
                procesarDerecha()

            if evento.key == pygame.K_DOWN:
                procesarAbajo()

            if evento.key == pygame.K_UP:
                procesarArriba()

            if evento.key == pygame.K_SPACE:
                procesarContinuar()

            if evento.key == pygame.K_LSHIFT:
                procesarPuntoIzquierda()

            if evento.key == pygame.K_RSHIFT:
                procesarPuntoDerecha()

            if evento.key == pygame.K_BACKSPACE:
                retrocederPunto()

            if evento.key == pygame.K_c:
                if estado == "jugando":
                    cambiarColor()

            if evento.key == pygame.K_s:
                if estado == "jugando":
                    cambiarSaque()

            if evento.key == pygame.K_l:
                if estado == 'jugando':
                    cambiarLado()

        if evento.type == pygame.KEYUP:

            if evento.key == pygame.K_1:
                tPres["1"] = False

            if evento.key == pygame.K_ESCAPE:
                tPres["esc"] = False

        #Eventos de joystick
        """ if evento.type == pygame.JOYAXISMOTION:
            
            if evento.axis == 0:

                if evento.value > 0.5:
                    procesarDerecha()
                    tPres['jDerecha'] = True
                else:
                    tPres['jDerecha'] = False

                if evento.value < -0.5:
                    procesarIzquierda()
                    tPres['jIzquierda'] = True
                else:
                    tPres['jIzquierda'] = False

            if evento.axis == 1:
                if evento.value > 0.5:
                    procesarAbajo()
                if evento.value < -0.5:
                    procesarArriba()

        if evento.type == pygame.JOYBUTTONDOWN:
            
            if evento.button == 9:
                procesarContinuar()

            if evento.button == 6:

                if not ( estado == estados[3] ) :
                    procesarContinuar()

                elif estado == estados[3] :
                    if tPres['jIzquierda'] == True :
                        procesarPuntoIzquierda()
                    elif tPres['jDerecha'] == True :
                        procesarPuntoDerecha()

            if evento.button == 7 :
                if tPres['j0'] == True :
                    retrocederPunto()

            if evento.button == 0 :
                tPres['j0'] = True

        if evento.type == pygame.JOYBUTTONUP:

            if evento.button == 0 :
                tPres['j0'] = False """

        #Eventos del ratón
        if evento.type == pygame.MOUSEBUTTONDOWN:

            print ('mouse: ', evento)

            if evento.button == 1 :
                if not ( estado == estados[3] ) :
                    procesarIzquierda()
                else:
                    procesarPuntoIzquierda()

            if evento.button == 3 :
                if not ( estado == estados[3] ) :
                    procesarDerecha()
                else:
                    procesarPuntoDerecha()
            
            if evento.button == 2 : 
                procesarContinuar()

            if evento.button == 5 :
                procesarAbajo()

            if evento.button == 4 :
                procesarArriba()    



        if evento.type == globales.QUIT:
            quit()

    if tPres["1"] and tPres["esc"]:
        quit()

    #Dibujado de puntero de joystick
    """ if estado == estados[3]:
        if tPres['jIzquierda'] :
            dibujarPuntero('+' , 'izquierda')
        elif tPres['jDerecha'] :
            dibujarPuntero('+' , 'derecha')
        elif tPres['j0'] :
            nAnotaciones = len(anotaciones)
            if nAnotaciones > 0 :
                if lado:
                    if anotaciones[nAnotaciones-1] == 1:
                        dibujarPuntero( '-' , 'izquierda' )
                    if anotaciones[nAnotaciones-1] == 2:
                        dibujarPuntero( '-' , 'derecha' )
                if not lado:
                    if anotaciones[nAnotaciones-1] == 2:
                        dibujarPuntero( '-' , 'izquierda' )
                    if anotaciones[nAnotaciones-1] == 1:
                        dibujarPuntero( '-' , 'derecha' ) """

    reproducirCola()

    dibujarCanvas()

    pygame.display.update()

    frames.tick(fps)
