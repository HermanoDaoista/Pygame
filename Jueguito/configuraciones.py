import pygame
from Constantes import *
from lo_del_profe import *

pygame.init()


boton_suma = crear_botones(IMAGEN_RESPUESTA,TAMAÑO_BOTON_VOLVER)

boton_resta = crear_botones(IMAGEN_RESPUESTA,TAMAÑO_BOTON_VOLVER)

boton_volver = crear_botones(IMAGEN_RESPUESTA,TAMAÑO_BOTON_VOLVER)


def mostrar_configuraciones(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_del_juego:dict) -> str:
    retorno = 'configurar'
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = 'salir'
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_suma['rectangulo'].collidepoint(evento.pos):
                subir_volumen(datos_del_juego)
                   
            elif boton_resta['rectangulo'].collidepoint(evento.pos):
                restar_volumen(datos_del_juego)   
                   
            elif boton_volver['rectangulo'].collidepoint(evento.pos):
                SONIDO_CLICK.play()
                retorno = 'menu'
    
    pantalla.blit(MI_FONDO,(0,0))
    boton_volver['rectangulo'] = pantalla.blit(boton_volver['superficie'],(10,10))
    mostrar_texto(boton_volver['superficie'],'ATRAS',(10,10),FUENTE_RESPUESTA,COLOR_NEGRO)
    boton_suma['rectangulo'] = pantalla.blit(boton_suma['superficie'],(20,200))
    mostrar_texto(boton_suma['superficie'],'VOL +',(10,10),FUENTE_FUENTE,COLOR_NEGRO)
    boton_resta['rectangulo'] = pantalla.blit(boton_resta['superficie'],(420,200))
    mostrar_texto(boton_resta['superficie'],'VOL -',(10,10),FUENTE_FUENTE,COLOR_NEGRO)
    mostrar_texto(pantalla,f'{datos_del_juego['volumen_musica']} %',(230,180),FUENTE_VOLUMEN,COLOR_NEGRO)

    return retorno                   