import pygame
from Constantes import *
from lo_del_profe import mostrar_texto
from cargar_ranking import *

pygame.init()
pygame.display.set_caption('RANKINGS')

boton_volver = crear_botones(IMAGEN_RESPUESTA,TAMAÑO_BOTON_VOLVER)
boton_ranking = crear_botones(IMAGEN_RANKING,(400,500))


def mostrar_rankings(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_del_juego:dict,rankings:list[list]):
    retorno = 'ranking'
    
    ranking = cargar_ranking(partidas)
    
    for evento in cola_eventos:
            if evento.type == pygame.QUIT:
                retorno = 'salir'  
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_volver['rectangulo'].collidepoint(evento.pos):
                    SONIDO_CLICK.play()
                    retorno = 'menu'
                    boton_ranking['superficie'] = pygame.transform.scale(IMAGEN_RANKING,(400,500))
                    
    
    pantalla.blit(MI_FONDO,(0,0))
    
    boton_ranking['rectangulo'] = pantalla.blit(boton_ranking['superficie'],(160,20))
    boton_volver['rectangulo'] = pantalla.blit(boton_volver['superficie'],(10,10))
    mostrar_texto(boton_volver['superficie'],'ATRAS',(10,10),FUENTE_RESPUESTA,COLOR_NEGRO)
    y_inicial = 100 
    espacio_entre_filas = 40
    boton_ranking['superficie'] = pygame.transform.scale(IMAGEN_RANKING,(400,500))
    for posicion, nombre in enumerate(ranking, start=1):
        texto = f"{posicion}. {nombre['usuario']} - {nombre['puntuacion']} pts - {fecha_formateada}"
        
        mostrar_texto(boton_ranking['superficie'], texto, (70, y_inicial),FUENTE_FUENTE_DOS,COLOR_NEGRO)
        y_inicial += espacio_entre_filas 
         

    return retorno