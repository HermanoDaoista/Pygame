
import pygame
from lo_del_profe import *
from Constantes import *


pygame.init()
pygame.mixer.init()
boton_vidas = crear_botones(IMAGEN_VIDAS,(100,100))
boton_mutear = crear_botones(IMAGEN_SONIDO,(50,50))
boton_puntuacion = crear_botones(IMAGEN_PUNTOS,(300,100))
carta_pregunta = crear_botones(IMAGEN_PREGUNTA,TAMANIO_PREGUNTA)
carta_pregunta['rectangulo'].center = (400, 140)

cartas_respuestas = []
for i in range(4):
    carta_respuesta = crear_botones(IMAGEN_RESPUESTA,TAMANIO_RESPUESTA)
    cartas_respuestas.append(carta_respuesta)


lista_preguntantos = []
leer_csv_preguntas('preguntas.csv',lista_preguntantos)
mezclar_lista(lista_preguntantos)
indice = 0
bandera_respuesta = False

evento_tiempo_1s = pygame.USEREVENT + 1
pygame.time.set_timer(evento_tiempo_1s,1000)

   

muteado = False
tiempo_respuesta = 10
contador_aciertos = 0

def mostrar_juego(pantalla:pygame.Surface, cola_eventos:list[pygame.event.Event],datos_juego:dict)->str:
    global muteado
    global indice
    global bandera_respuesta
    global tiempo_respuesta
    global contador_aciertos
    

    
    retorno = 'jugando'
    pregunta_actual = lista_preguntantos[indice]
    if datos_juego['vidas'] == 0:
        retorno = 'fin'
    if bandera_respuesta:
        pygame.time.delay(700)
        bandera_respuesta = False

    carta_pregunta = crear_botones(IMAGEN_PREGUNTA,TAMANIO_PREGUNTA)
    carta_pregunta['rectangulo'].center = (400, 140)

    for i in range(4):
        cartas_respuestas[i]['superficie'] = pygame.transform.scale(IMAGEN_RESPUESTA,TAMANIO_RESPUESTA)
 
    boton_vidas = crear_botones(IMAGEN_VIDAS,(60,60))
   
    for evento in cola_eventos:
            if evento.type == pygame.QUIT:
                retorno = 'salir'
            if evento.type == evento_tiempo_1s:
                tiempo_respuesta -= 1
                 
            if tiempo_respuesta == 0:
                SONIDO_CLICK.play()
                datos_juego['vidas'] -= 1
                indice += 1 
                tiempo_respuesta = 10
                 
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                print(evento.pos)
                if boton_mutear['rectangulo'].collidepoint(evento.pos):
                    if muteado:
                        desmutear_musica()
                        SONIDO_PLOC.play()
                        boton_mutear['superficie'] = pygame.transform.scale(IMAGEN_SONIDO,(50,50))  
                    else:
                        pausar_musica()
                        SONIDO_PLOC.play()
                        boton_mutear['superficie'] = pygame.transform.scale(IMAGEN_MUTED,(50,50))
                    
                muteado = not muteado       
                            
                
                for i in range(len(cartas_respuestas)):
                    if cartas_respuestas[i]['rectangulo'].collidepoint(evento.pos):
                        respuesta_seleccionada = (i+1)
              
                        if verificar_respuesta(datos_juego,pregunta_actual,respuesta_seleccionada):
                            cartas_respuestas[i]['superficie'] = pygame.transform.scale(IMAGEN_ACIERTO,TAMANIO_RESPUESTA)
                            boton_puntuacion['superficie'] = pygame.transform.scale(IMAGEN_PUNTOS,(300,100))
                            SONIDO_ACIERTO.play()
                            contador_aciertos +=1
                            if contador_aciertos == 5:
                                datos_juego['vidas'] +=1
                                SONIDO_VIDA.play()
                                contador_aciertos = 0
                                
                            tiempo_respuesta = 10
                        else:
                            SONIDO_ERROR.play() 
                            cartas_respuestas[i]['superficie'] = pygame.transform.scale(IMAGEN_ERROR,TAMANIO_RESPUESTA)
                            boton_puntuacion['superficie'] = pygame.transform.scale(IMAGEN_PUNTOS,(300,100))
                            contador_aciertos = 0
                            tiempo_respuesta = 10
                            
                            
                        indice += 1
                           
                        if indice == len(lista_preguntantos):
                            indice = 0
                            mezclar_lista(lista_preguntantos)       
                        bandera_respuesta = True
                    

    mostrar_texto_margen(carta_pregunta['superficie'],pregunta_actual['pregunta'],FUENTE_PREGUNTA,COLOR_NEGRO,(100,100,350,400),padding=10)
                
    mostrar_texto(cartas_respuestas[0]['superficie'],pregunta_actual['respuesta_1'],(20,20),FUENTE_RESPUESTA,COLOR_NEGRO)
    mostrar_texto(cartas_respuestas[1]['superficie'],pregunta_actual['respuesta_2'],(20,20),FUENTE_RESPUESTA,COLOR_NEGRO)
    mostrar_texto(cartas_respuestas[2]['superficie'],pregunta_actual['respuesta_3'],(20,20),FUENTE_RESPUESTA,COLOR_NEGRO)
    mostrar_texto(cartas_respuestas[3]['superficie'],pregunta_actual['respuesta_4'],(20,20),FUENTE_RESPUESTA,COLOR_NEGRO)
    pantalla.blit(MI_FONDO,(0,0))
    pantalla.blit(carta_pregunta['superficie'], carta_pregunta['rectangulo'])
    mostrar_texto(pantalla,f'TIEMPO {tiempo_respuesta}',(360,40),FUENTE_RESPUESTA,COLOR_NEGRO)
    mostrar_texto(boton_vidas['superficie'],f'{datos_juego["vidas"]}',(22,15),FUENTE_VIDAS,COLOR_NEGRO)
    mostrar_texto(boton_puntuacion['superficie'],f'{datos_juego['puntuacion']}',(100,40),FUENTE_FUENTE_TRES,COLOR_NEGRO)
    boton_vidas['rectangulo'] = pantalla.blit(boton_vidas['superficie'],(30,65))
    boton_puntuacion['rectangulo'] = pantalla.blit(boton_puntuacion['superficie'],(250,450))
    
                        
                            
                        
                      
    
    
 
    cartas_respuestas[0]['rectangulo'] = pantalla.blit(cartas_respuestas[0]['superficie'],(125,315))
    cartas_respuestas[1]['rectangulo'] = pantalla.blit(cartas_respuestas[1]['superficie'],(400,315))
    cartas_respuestas[2]['rectangulo'] = pantalla.blit(cartas_respuestas[2]['superficie'],(125,385))
    cartas_respuestas[3]['rectangulo'] = pantalla.blit(cartas_respuestas[3]['superficie'],(400,385))
    boton_mutear['rectangulo'] = pantalla.blit(boton_mutear['superficie'],(750,30))
    return retorno