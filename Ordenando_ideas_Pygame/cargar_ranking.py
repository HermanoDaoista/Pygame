import pygame
from Constantes import *
from lo_del_profe import *
from cargar_ranking import *
from datetime import datetime
#imagen_respuesta = pygame.image.load('respuestax.jpg')

pygame.init()
pygame.display.set_caption('GAME OVER')
boton_volver = crear_botones(IMAGEN_RESPUESTA,TAMAÑO_BOTON_VOLVER)

boton_aceptar = crear_botones(IMAGEN_RESPUESTA,TAMAÑO_BOTON_VOLVER)
boton_puntuacion = crear_botones(IMAGEN_PUNTOS,(300,100))

caja_texto = crear_botones(IMAGEN_RESPUESTA,CUADRO_TEXTO)

nombre = ''
partidas = 'ejemplo.json'
fecha_actual = datetime.now()

# Formatear la fecha como "DD/MM/AAAA"
fecha_formateada = fecha_actual.strftime("%d/%m/%Y")




def mostrar_juego_terminado(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_del_juego:dict,ranking:dict)->str:
    
    global nombre
    retorno = 'fin'
    
    for evento in cola_eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_aceptar['rectangulo'].collidepoint(evento.pos):
                SONIDO_CLICK.play()
                caja_texto['superficie'] = pygame.transform.scale(IMAGEN_RESPUESTA, CUADRO_TEXTO) 
                ranking_actualizado = actualizar_ranking(ranking,nombre,datos_del_juego['puntuacion'],fecha_formateada)
                guardar_ranking(partidas,ranking_actualizado)
                boton_puntuacion['superficie'] = pygame.transform.scale(IMAGEN_PUNTOS,(300,100))
                datos_del_juego['puntuacion'] = 0
                nombre = ""  
                retorno = 'ranking'
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_volver['rectangulo'].collidepoint(evento.pos):
                SONIDO_CLICK.play()
                nombre = ""  
                caja_texto['superficie'] = pygame.transform.scale(IMAGEN_RESPUESTA, CUADRO_TEXTO)  # Limpiar la caja de texto
                retorno = 'menu'
                
        if evento.type == pygame.KEYDOWN:
            letra_presionada = pygame.key.name(evento.key)
            block_mayus = pygame.key.get_mods() and pygame.KMOD_CAPS
            if letra_presionada == 'space':
                nombre += ' '   
            if letra_presionada == 'backspace' and len(nombre) > 0:
                nombre = nombre[0:-1]
                caja_texto['superficie'] = pygame.transform.scale(IMAGEN_RESPUESTA, CUADRO_TEXTO)    
            if len(letra_presionada) == 1:
                if block_mayus != 0:
                    nombre+= letra_presionada.upper()
                else:
                    nombre += letra_presionada 
                    
        if evento.type == pygame.QUIT:
            retorno = 'salir'
    pantalla.blit(MI_FONDO,(0,0))
                
                
    caja_texto['rectangulo'] = pantalla.blit(caja_texto['superficie'],(200,200))
    mostrar_texto(caja_texto['superficie'],nombre,(10,0),FUENTE_TRES,COLOR_NEGRO)
    mostrar_texto(pantalla,f'Usted obtuvo  {datos_del_juego['puntuacion']}  puntos',(250,100),FUENTE_TRES)
    boton_volver['rectangulo'] = pantalla.blit(boton_volver['superficie'],(10,10))
    mostrar_texto(boton_volver['superficie'],'ATRAS',(10,10),FUENTE_RESPUESTA,COLOR_NEGRO)
    boton_aceptar['rectangulo'] = pantalla.blit(boton_aceptar['superficie'],(10,100))
    mostrar_texto(boton_aceptar['superficie'],'ACEPTAR',(10,10),FUENTE_RESPUESTA,COLOR_NEGRO)
    return retorno