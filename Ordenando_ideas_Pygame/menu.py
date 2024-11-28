import pygame
from Constantes import *
import random
from lo_del_profe import *

pygame.init()
pygame.display.set_caption('MENU')

# fuente_menu = pygame.font.SysFont('Arial Narrow',30)
# imagen_menu = pygame.image.load('respuestax.jpg')
carta_menu = []
for i in range(4):
    boton_menu = crear_botones(IMAGEN_RESPUESTA,(400,100))
    carta_menu.append(boton_menu)
    

def mostrar_menu(pantalla:pygame.surface,cola_evento:list[pygame.event.Event])-> str:
    retorno = 'menu'
    for evento in cola_evento:
        if evento.type == pygame.QUIT:
            retorno = 'salir'
        if evento.type == pygame.MOUSEBUTTONDOWN:  
            for i in range(len(carta_menu)):
                if carta_menu[i]['rectangulo'].collidepoint(evento.pos):
                    if i == BOTON_JUGAR:
                        retorno = 'jugando'
                        
                    elif i == BOTON_CONFIG:
                        retorno = 'configurar'
                    elif i == BOTON_RANKING:
                        
                        retorno = 'ranking'
                    elif i == BOTON_SALIR:
                        retorno = 'salir'          
    mi_fondo = pygame.image.load('fondo.webp') 
    mi_fondo = pygame.transform.scale(mi_fondo,(VENTANA))  
    pantalla.blit(mi_fondo,(0,0))
    carta_menu[BOTON_JUGAR]['rectangulo'] = pantalla.blit(carta_menu[BOTON_JUGAR]['superficie'],(200,50)) 
    carta_menu[BOTON_CONFIG]['rectangulo'] = pantalla.blit(carta_menu[BOTON_CONFIG]['superficie'],(200,160))        
    carta_menu[BOTON_RANKING]['rectangulo'] = pantalla.blit(carta_menu[BOTON_RANKING]['superficie'],(200,270))        
    carta_menu[BOTON_SALIR]['rectangulo'] = pantalla.blit(carta_menu[BOTON_SALIR]['superficie'],(200,380))        
    mostrar_texto(carta_menu[BOTON_JUGAR]['superficie'],'JUGAR',(65,10),FUENTE_MENU,MARRON_OSCURO_TRANSPARENTE)
    mostrar_texto(carta_menu[BOTON_CONFIG]['superficie'],'CONFIG',(65,10),FUENTE_MENU,MARRON_OSCURO_TRANSPARENTE)
    mostrar_texto(carta_menu[BOTON_RANKING]['superficie'],'RANKINGS',(65,10),FUENTE_MENU,MARRON_OSCURO_TRANSPARENTE)
    mostrar_texto(carta_menu[BOTON_SALIR]['superficie'],'SALIR',(65,10),FUENTE_MENU,MARRON_OSCURO_TRANSPARENTE)

    return retorno


