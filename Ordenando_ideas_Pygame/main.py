import pygame
from Constantes import *
from lo_del_profe import *
from menu import *
from juego import *
from rankings import *
from configuraciones import *
from cargar_ranking import *


pygame.init()

pygame.display.set_caption('Mi primer jueguito')
icono = pygame.image.load('icono.webp')
pygame.display.set_icon(icono)


clock = pygame.time.Clock()
pygame.mixer.init()
bandera_musica = False
bandera_vida = False
partidas = 'ejemplo.json'
corriendo = True

datos_del_juego = {'puntuacion': 0,'vidas': CANTIDAD_DE_VIDAS,'usuario':'','volumen_musica':10}

ventana_actual = 'menu'
while corriendo:
    cola_eventos = pygame.event.get() 
    clock.tick(FPS)

    if ventana_actual == 'menu':
        ventana_actual = mostrar_menu(PANTALLA,cola_eventos)
        ranking = cargar_ranking(partidas)
    elif ventana_actual == 'jugando':
        
        if bandera_vida == False:
            datos_del_juego['vidas'] += 3
            datos_del_juego['puntuacion'] = 0
            bandera_vida = True
            
        if bandera_musica == False:
            bandera_musica = True
        
            volumen_real = datos_del_juego['volumen_musica'] / 100
            cargar_musica('musica.mp3',volumen_real)
           
        ventana_actual = mostrar_juego(PANTALLA,cola_eventos,datos_del_juego)
       
    elif ventana_actual == 'configurar':
        ventana_actual = mostrar_configuraciones(PANTALLA,cola_eventos,datos_del_juego) 
            
    elif ventana_actual == 'ranking':
        bandera_vida = False
        ranking = cargar_ranking(partidas)

        ventana_actual = mostrar_rankings(PANTALLA,cola_eventos,datos_del_juego,ranking)
        
    elif ventana_actual == 'fin':
        
        if bandera_musica == True:
            pygame.mixer.music.stop()
            bandera_musica = False
        ventana_actual = mostrar_juego_terminado(PANTALLA,cola_eventos,datos_del_juego,ranking)
    elif ventana_actual == 'salir':
        
        corriendo = False
         
    pygame.display.flip()  
pygame.quit()      
    

        
         
        
