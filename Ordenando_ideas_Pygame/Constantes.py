import pygame

pygame.init()

FUENTE_MENU = pygame.font.Font('madera.ttf',55)
MARRON_CLARO = (210, 180, 250) 
MARRON_OSCURO = (139, 69, 19)
COLOR_BLANCO = (255,255,255)
COLOR_NEGRO = (0,0,0)
COLOR_ROJO = (255,0,0)
COLOR_VERDE = (0,255,0)
COLOR_AZUL = (0,0,255)
COLOR_VIOLETA = (134,23,219)
MARRON_OSCURO_TRANSPARENTE = (139, 69, 19, 128) 
ANCHO = 800
ALTO = 600
VENTANA = (ANCHO,ALTO)
FPS = 60
###################
TAMANIO_PREGUNTA = (600,300)
TAMANIO_RESPUESTA = (250,60)
# TAMANIO_BOTON = (250,60)
# CUADRO_TEXTO = (250,50)
############################
CANTIDAD_DE_VIDAS = 0
PUNTUACION_ACIERTOS = 100
PUNTUACION_ERROR = 25
TAMAÑO_BOTON = (250,60)
CUADRO_TEXTO = (250,50)
TAMAÑO_BOTON_VOLUMEN = (60,60)
TAMAÑO_BOTON_VOLVER = (100,40)

BOTON_JUGAR = 0
BOTON_CONFIG = 1
BOTON_RANKING = 2
BOTON_SALIR = 3
FUENTE_TRES = pygame.font.Font('fuente3.ttf',50)
FUENTE_VOLUMEN =  pygame.font.Font('fuente1.ttf',60)
FUENTE_PREGUNTA = pygame.font.SysFont('Arial Narrow',40)
FUENTE_RESPUESTA = pygame.font.SysFont('Arial Narrow',22)
FUENTE_FUENTE = pygame.font.SysFont('fuente2',30)
FUENTE_MENUDO = pygame.font.SysFont('Arial Narrow',30)
FUENTE_FUENTE_DOS = pygame.font.SysFont('fuente2',25)
FUENTE_VIDAS = pygame.font.SysFont('otra.ttf',40)
FUENTE_FUENTE_TRES = pygame.font.SysFont('fuente2',50)


SONIDO_CLICK = pygame.mixer.Sound('click.ok.mp3') 

SONIDO_PLOC = pygame.mixer.Sound('bamboo.mp3')
SONIDO_PLOC.set_volume(0.5) 
SONIDO_ACIERTO = pygame.mixer.Sound('acerto.mp3')
SONIDO_ERROR = pygame.mixer.Sound('error.mp3')
SONIDO_VIDA = pygame.mixer.Sound('vida.mp3')
CLICK_SONIDO = pygame.mixer.Sound('click.ok.mp3')
MI_FONDO = pygame.image.load('fondo.webp') 
MI_FONDO = pygame.transform.scale(MI_FONDO,(VENTANA))

IMAGEN_VIDAS = pygame.image.load('corazon.webp')
#IMAGEN_VIDAS = pygame.transform.scale(IMAGEN_VIDAS,(100,100))
IMAGEN_PUNTOS = pygame.image.load('asi.webp')
#IMAGEN_PUNTOS = pygame.transform.scale(IMAGEN_PUNTOS,(100,50))
IMAGEN_PREGUNTA = pygame.image.load('preguntax.jpg')
IMAGEN_RESPUESTA = pygame.image.load('respuestax.jpg')
IMAGEN_ACIERTO = pygame.image.load('acerto_sir.jpg')
IMAGEN_ERROR = pygame.image.load('error_mal.jpg')
IMAGEN_RANKING = pygame.image.load('tabla_ranking.png')
IMAGEN_RANKING = pygame.transform.scale(IMAGEN_RANKING,(400,500))
IMAGEN_SONIDO =  pygame.image.load('sonido.jpg')
IMAGEN_SONIDO = pygame.transform.scale(IMAGEN_SONIDO,(60,60))
IMAGEN_MUTED =  pygame.image.load('muteado.jpg')
IMAGEN_MUTED = pygame.transform.scale(IMAGEN_MUTED,(60,60))
###########################################
PANTALLA = pygame.display.set_mode(VENTANA)

