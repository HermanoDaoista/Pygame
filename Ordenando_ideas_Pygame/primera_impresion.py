# #
# import pygame
# pygame.init()

# screen = pygame.display.set_mode((400, 300))
# pygame.display.set_caption("Hola, Pygame!")

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
# pygame.quit()

###########################################################################################
#
import pygame 
from Constantes import *

pygame.init()

pygame.display.set_caption('mi primer juego Dao')

icono = pygame.image.load('icono.png')
pygame.display.set_icon(icono)

#pantalla
pantalla = pygame.display.set_mode((VENTANA))
corriendo = True
contador = 0
# mi_superficie = pygame.Surface((100,100))

# mi_superficie.fill(COLOR_VIOLETA)

mi_superficie = pygame.image.load('pitfall.jpg')
mi_superficie = pygame.transform.scale(mi_superficie,(80,100))
fondo = pygame.image.load('pagoda.png')
fondo = pygame.transform.scale(fondo,VENTANA)
#texto
fuente = pygame.font.SysFont('Arial',25)
texto = fuente.render(f'CONTADOR: {contador}', False, COLOR_NEGRO)
#Sonido 
sonido_click = pygame.mixer.Sound('click.mp3')
sonido_click.set_volume(1)

#Musica de fondo
pygame.mixer.init() # -> musica defondo
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)



#relog -> capea fps
clock = pygame.time.Clock()
#Evento de tiempo
evento_tiempo_1s = pygame.USEREVENT
pygame.time.set_timer(evento_tiempo_1s,1000)
evento_tiempo_10s = pygame.USEREVENT + 1
pygame.time.set_timer(evento_tiempo_10s,10000)
cantidad_segundos = 0
#bucle principal -> 
while corriendo:
    clock.tick(FPS)  #-> msi afterburner ajjaja
    #print(contador)
    contador += 1
    
    #manej de ventos
    for evento in pygame.event.get():
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print('se hizo click')
            print(evento.pos)
            sonido_click.stop()
            sonido_click.play(2)

        if evento.type == pygame.QUIT:
            print('salimos')
            corriendo = False 
        if evento.type == evento_tiempo_1s:
            print('paso un segundo')  
            cantidad_segundos += 1
        if evento.type == evento_tiempo_10s:
            print('pasaron 10 segundos')

    #actualizar juego
    texto = fuente.render(f'CONTADOR: {cantidad_segundos}', False, COLOR_NEGRO)


    #dibujar elementos de la pantalla
    #pantalla.fill(COLOR_BLANCO)
    pantalla.blit(fondo,(0,0))
    #un circulo rojo
    #pygame.draw.circle(pantalla,COLOR_ROJO,(250,50),50)
    #rectangulo negro
    #pygame.draw.rect(pantalla,COLOR_VERDE,(150,100,50,70))
    #imagenes personalizadas
    pantalla.blit(mi_superficie,(50,50))

    pantalla.blit(texto,(10,10))
    



    #actualizar pantalla -> ultima linea del while 
    pygame.display.flip()

pygame.quit()
