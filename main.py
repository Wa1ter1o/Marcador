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
pygame.mixer.set_reserved(0)

pygame.mouse.set_visible(False)

frames = tiempo.Clock() 
fps = 30                            #velocidad de actualización en frames por segundo
velAnim = 1                         #tiempo en segundos para hacer cada animación
pasoAnim = 80                       #incremental de movimiento para todas las animaciones en pixels

milisegundos = tiempo.get_ticks()

ancho, alto = 1920, 1080
#obtener resolución de pantalla
infoPantalla = pygame.display.Info()
#print(infoPantalla)
#escala de pantalla
escala = infoPantalla.current_w / ancho
print("escala: " + str(escala))
escala = 0.7

ventana = pygame.display.set_mode( ( int( ancho * escala  ), int( alto * escala ) ) )
canvas = pygame.Surface( (ancho, alto) )

pygame.display.set_caption( 'Marcador para tenis de mesa' )

#-------------------------Cargando Imágenes y efectos de sonido--------------------------------------------------------------

fondoOriginal = pygame.image.load( "assets/img/fondo.jpg" )
fondo = pygame.transform.scale(fondoOriginal, ( int( ancho ) , int( alto  ) ) )

azul = pygame.image.load( "assets/img/azul.png" )
rojo = pygame.image.load( "assets/img/rojo.png" )
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
    'punto' : mixer.Sound('assets/sonidos/fx/punto.wav'),
    'set' : mixer.Sound('assets/sonidos/fx/set.wav') 
    }

rutas = list(Path('assets/sonidos/frases/Mariano/un punto').iterdir())
unPunto = []
for ruta in rutas:
    unPunto.append(mixer.Sound(ruta))

rutas = list(Path('assets/sonidos/frases/Mariano/dos puntos').iterdir())
dosPuntos = []
for ruta in rutas:
    dosPuntos.append(mixer.Sound(ruta))

rutas = list(Path('assets/sonidos/frases/Mariano/cuatro puntos').iterdir())
cuatroPuntos = []
for ruta in rutas:
    cuatroPuntos.append(mixer.Sound(ruta))

rutas = list(Path('assets/sonidos/frases/Mariano/cinco puntos').iterdir())
cincoPuntos = []
for ruta in rutas:
    cincoPuntos.append(mixer.Sound(ruta))

rutas = list(Path('assets/sonidos/frases/Mariano/seis puntos').iterdir())
seisPuntos = []
for ruta in rutas:
    seisPuntos.append(mixer.Sound(ruta))

rutas = list(Path('assets/sonidos/frases/Mariano/siete puntos').iterdir())
sietePuntos = []
for ruta in rutas:
    sietePuntos.append(mixer.Sound(ruta))

rutas = list(Path('assets/sonidos/frases/Mariano/dos puntos').iterdir())
DosPuntos = []
for ruta in rutas:
    DosPuntos.append(mixer.Sound(ruta))

rutas = list(Path('assets/sonidos/frases/Mariano/dos puntos').iterdir())
DosPuntos = []
for ruta in rutas:
    DosPuntos.append(mixer.Sound(ruta))

rutas = list(Path('assets/sonidos/frases/Mariano/dos puntos').iterdir())
DosPuntos = []
for ruta in rutas:
    DosPuntos.append(mixer.Sound(ruta))

rutas = list(Path('assets/sonidos/frases/Mariano/ocho puntos').iterdir())
ochoPuntos = []
for ruta in rutas:
    ochoPuntos.append(mixer.Sound(ruta))

rutas = list(Path('assets/sonidos/frases/Mariano/nueve puntos').iterdir())
nuevePuntos = []
for ruta in rutas:
    nuevePuntos.append(mixer.Sound(ruta))

rutas = list(Path('assets/sonidos/frases/Mariano/diez puntos').iterdir())
diezPuntos = []
for ruta in rutas:
    diezPuntos.append(mixer.Sound(ruta))



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
        if letra == '\\' :
            break

        nombreInvertido = nombreInvertido + letra

    for letra in reversed(nombreInvertido):
        nombre = nombre + letra

    nombreCarpetas.append(nombre)

canalComentario = mixer.Channel(0)
reproducirComentario = []
reproducirEfecto = []
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& JUGADORES $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

jugadores = [
     { "nombre" : "Alejandro" , "tts" : mixer.Sound('assets/sonidos/nombres/Alejandro.wav') } ,
     { "nombre" : "Diego" , "tts" : mixer.Sound('assets/sonidos/nombres/Diego.wav') } ,
     { "nombre" : "Javi" , "tts" : mixer.Sound('assets/sonidos/nombres/Javi.wav') } ,
     { "nombre" : "Jugador Uno" , "tts" : mixer.Sound('assets/sonidos/nombres/Jugador uno.wav') } ,
     { "nombre" : "Jugador Dos" , "tts" : mixer.Sound('assets/sonidos/nombres/Jugador dos.wav') } ,
     { "nombre" : "Lilly" , "tts" : mixer.Sound('assets/sonidos/nombres/Lilly.wav') } ,
     { "nombre" : "Pablo" , "tts" : mixer.Sound('assets/sonidos/nombres/Pablo.wav') } ,
     { "nombre" : "Walter" , "tts" : mixer.Sound('assets/sonidos/nombres/Walter.wav') } ,
     { "nombre" : "Willy" , "tts" : mixer.Sound('assets/sonidos/nombres/Willy.wav') } ,
     { "nombre" : "William" , "tts" : mixer.Sound('assets/sonidos/nombres/William.wav') } 
     ]

nombres = []
for jugador in jugadores:
    nombres.append(jugador['nombre'])

#*****************************VARIABLES DEL JUEGO****************************************************************************

iu = { 'fuente' : 'OCR A Extended' }

jugadorUno = clases.Jugador(pygame, "Jugador Uno", mixer.Sound('assets/sonidos/nombres/Jugador uno.wav'),True, azul, "izquierda")
jugadorDos = clases.Jugador(pygame, "Jugador Dos", mixer.Sound('assets/sonidos/nombres/Jugador dos.wav') ,False, rojo, "derecha")

pelota = clases.pelota( "izquierda" )


sets = 1                        #sets a jugar
puntosPorSet = 11               #puntos a jugar por set
cambioSaque = 2                 #número de saques para hacer cambio de saque
lado = True                     #define de que lado se encuentra cada jugador
saque = True                    #si es True el saque le corresponde al jugador uno


puntosTotalesSet = 0

estados = ( "inicio" , "post juego" , "cuenta",  "jugando" , "post nuevo set" , "pausa" , "post fin" , "fin" )

estado = estados[ 0 ]

tPres = { "1" : False , "esc" : False , }

botones = False
arbitro = False

segInicioCuentaRegresiva = None
contandoSegudos = False

beeps = [ 0, 0, 0, 0 ]

#////////////////////////////// LISTAS DE MENÚ //////////////////////////////////////////////////////////////////////////////

indicesMenu = { 'inicio' : 0 , 'pausa' : 0 }

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

    if estado == estados[ 2 ] :
        cuentaRegresiva()

    if estado == estados[5] :
        canvas.blit( menuPausa.generarImagen(), menuPausa.pos)

def tocarMusica() :

    if musica :
        mixer.music.load(rutasMusica[indiceMusicaFondo][random.randint(0, len(rutasMusica[indiceMusicaFondo]) - 1)])
        mixer.music.play(-1)

def pausarMusica() :

    mixer.music.pause()

def seguirMusica():

    if musica :
        mixer.music.unpause()

def setearVolumen():

    mixer.music.set_volume(volMusica / 10)


def reproducirCola():
    global reproducirComentario, reproducirEfecto

    if len(reproducirComentario) > 0 and not canalComentario.get_busy():
        audio = reproducirComentario.pop(0)
        audio.set_volume( volNarracion / 10 )
        audio.play(0)
    else:
        print(mixer.get_busy())

    if len(reproducirEfecto) > 0 :
        audio = reproducirEfecto.pop(0)
        audio.set_volume( volEfectos / 10 )
        audio.play()


def cuentaRegresiva():
    global segInicioCuentaRegresiva, contandoSegudos, estado, beeps

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
        if datosInicio[4]['indice'] == 2:
            if random.randint(0, 1) == 1:
                cambiarSaque()
        beeps[0] = 1
        
    if segFaltantes < 3 and beeps[1] == 0 :
        audiofx['bep'].set_volume(volEfectos)
        audiofx['bep'].play()
        if datosInicio[4]['indice'] == 2:
            if random.randint(0, 1) == 1:
                cambiarSaque()
        beeps[1] = 1

    if segFaltantes < 2 and beeps[2] == 0 :
        audiofx['bep'].set_volume(volEfectos)
        audiofx['bep'].play()
        if datosInicio[4]['indice'] == 2:
            if random.randint(0, 1) == 1:
                cambiarSaque()
        beeps[2] = 1

    if segFaltantes < 1 and beeps[3] == 0 :
        audiofx['bep2'].set_volume(volEfectos)
        audiofx['bep2'].play()
        if datosInicio[4]['indice'] == 2:
            if random.randint(0, 1) == 1:
                cambiarSaque()
        beeps[3] = 1
    
    if segFaltantes < 0.2 : 
        estado = estados[3]
        contandoSegudos = False
        beeps = [ 0, 0, 0, 0]
        
        setearVolumen()
        tocarMusica()



def comprobarReglas():


    if ( puntosPorSet - jugadorUno.puntos <= 1 ) and ( puntosPorSet - jugadorDos.puntos <= 1 ) :
        cambiarSaque()
    elif puntosTotalesSet % cambioSaque == 0:
        cambiarSaque()

    pInvParaGanar = ( puntosPorSet + 1 ) / 2 + 1
    if ( jugadorUno.puntos == pInvParaGanar or jugadorDos.puntos == pInvParaGanar) and \
        ( jugadorUno.puntos == 0 or jugadorDos.puntos == 0 ) :
        anotarSet()
        cambiarLado()

    if ( (jugadorUno.puntos >= puntosPorSet ) or ( jugadorDos.puntos >= puntosPorSet ) ) \
        and abs( jugadorUno.puntos - jugadorDos.puntos ) >= 2 :
        anotarSet()
        cambiarLado()

def agregarComentario(clave, puntos):

    if clave == 'punto':
        if puntos == 1:
            reproducirComentario.append(unPunto[random.randint(0, len(unPunto)-1)])


def anotarPunto(jugador):
    global puntosTotalesSet

    if jugador == 1:
        jugadorUno.anotarPunto()
        jugadorUno.puntosSeguidos += 1
        jugadorDos.puntosSeguidos = 0
        if narracion :
            reproducirComentario.append(jugadorUno.tts)
            agregarComentario('punto', jugadorUno.puntosSeguidos)

    if jugador == 2:
        jugadorDos.anotarPunto()
        jugadorDos.puntosSeguidos += 1
        jugadorUno.puntosSeguidos = 0
        if narracion :
            reproducirComentario.append(jugadorDos.tts)
            agregarComentario('punto', jugadorDos.puntosSeguidos)

    puntosTotalesSet += 1

    audiofx['punto'].set_volume( volEfectos / 10 )
    audiofx['punto'].play()

    comprobarReglas()

def anotarSet():

    if jugadorUno.puntos > jugadorDos.puntos :
        jugadorUno.anotarSet()

    elif jugadorDos.puntos > jugadorUno.puntos :
        jugadorDos.anotarSet()

    iniciarPuntos()

    reproducirEfecto.append(audiofx['set'])
    

def iniciarMarcadores():
    global puntosTotalesSet

    jugadorUno.puntos = 0
    jugadorUno.sets = 0

    jugadorDos.puntos = 0
    jugadorDos.sets = 0

    puntosTotalesSet = 0

def iniciarPuntos():
    global puntosTotalesSet

    jugadorUno.puntos = 0

    jugadorDos.puntos = 0

    puntosTotalesSet = 0


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
            setearVolumen()

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

            setearVolumen()

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


def procesarContinuar():
    global estado

#                0             1            2          3              4              5           6         7
# estados = ( "inicio" , "post juego" , "cuenta",  "jugando" , "post nuevo set" , "pausa" , "post fin" , "fin" )

    if estado == estados[0]:    # Inicio
        estado = estados[2]     # Post juego

    elif estado == estados[1]:  # Post juego
        estado = estados[2]     # cuenta

    elif estado == estados[3]:  # jugando
        estado = estados[5]     # pausa
        pausarMusica()

    elif estado == estados[5] and datosPausa[4]['dato'] == 'Si': # Nuevo Juego
        iniciarMarcadores()
        estado = estados[0]
        datosPausa[4]['dato'] = 'No'

    elif estado == estados[5]:  # pausa
        estado = estados[3]     # jugando
        seguirMusica()
    
    elif estado == estados[4]:  # post nuevo set
        estado = estados[2]     # cuenta

    elif estado == estados[6]:  # post fin
        estado = estados[7]     # fin

    elif estado == estados[7]:  # fin
        estado = estados[0]     # inicio
        iniciarMarcadores()

    print ( estado )

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
    pygame.mixer.quit()
    pygame.font.quit()
    pygame.quit()
    sys.exit()

#----------------------------------CICLO PRINCIPAL---------------------------------------------------------------------------    

setearVolumen()
dibujarFondo()


while True:

    milisegundos = tiempo.get_ticks()
    mover()
    dibujarFondo()
    dibujarJugadores()
    dibujarMenu()
    reproducirCola()

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

            if evento.key == pygame.K_c:
                if estado == "jugando":
                    cambiarColor()

            if evento.key == pygame.K_s:
                if estado == "jugando":
                    cambiarSaque()

        if evento.type == pygame.KEYUP:

            if evento.key == pygame.K_1:
                tPres["1"] = False

            if evento.key == pygame.K_ESCAPE:
                tPres["esc"] = False

        if evento.type == globales.QUIT:
            quit()

    if tPres["1"] and tPres["esc"]:
        quit()

    dibujarCanvas()

    pygame.display.update()

    frames.tick(fps)
