import pygame
from lo_del_profe import *
from preguntas import *

pygame.init()

#Configuraciones basicas de mi juego
pygame.display.set_caption("MI PRIMER JUEGO 313")
icono = pygame.image.load("icono.png")
pygame.display.set_icon(icono)

#Configurar la pantalla
pantalla = pygame.display.set_mode(VENTANA)
corriendo = True

#Crear elementos para mi juego

carta_pregunta = {}
carta_pregunta["superficie"] = pygame.Surface(TAMANIO_PREGUNTA)
carta_pregunta["rectangulo"] = carta_pregunta["superficie"].get_rect()

cartas_respuestas = []

for i in range(3):
    carta_respuesta = {}
    carta_respuesta["superficie"] = pygame.Surface(TAMANIO_RESPUESTA)
    carta_respuesta["rectangulo"] = carta_respuesta["superficie"].get_rect()
    cartas_respuestas.append(carta_respuesta)


#Creo un reloj 
clock = pygame.time.Clock()

fuente_pregunta = pygame.font.SysFont("Arial Narrow",30)
fuente_respuesta = pygame.font.SysFont("Arial Narrow",22)
fuente_texto = pygame.font.SysFont("Arial Narrow",25)
indice = 0
datos_juego = {"puntuacion":0,"vidas":CANTIDAD_DE_VIDAS,"usuario":""}
mezclar_lista(lista_preguntas)

#Sonidos
click_acierto = pygame.mixer.Sound("click.ok.mp3")
click_error = pygame.mixer.Sound("error.mp3")

bandera_respuesta = False

while corriendo:
    clock.tick(FPS)
    
    pregunta_actual = lista_preguntas[indice]
    
    if bandera_respuesta:
        pygame.time.delay(500)
        bandera_respuesta = False
    
    #SOLO HACEMOS ESTO PORQUE NO MANIPULAMOS IMAGENES
    carta_pregunta["superficie"].fill(COLOR_ROJO)
    for i in range(len(cartas_respuestas)):
        cartas_respuestas[i]["superficie"].fill(COLOR_AZUL)
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            print("SALIENDO")
            corriendo = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(cartas_respuestas)):
                if cartas_respuestas[i]["rectangulo"].collidepoint(evento.pos):
                    respuesta_seleccionada = (i + 1)
                    print(f"LE DIO CLICK A LA RESPUESTA : {respuesta_seleccionada}")
                    
                    if verificar_respuesta(datos_juego,pregunta_actual,respuesta_seleccionada):
                        print("RESPUESTA CORRECTA")
                        #Ustedes van a manejar una imagen para esto
                        cartas_respuestas[i]["superficie"].fill(COLOR_VERDE)
                        click_acierto.play()
                    else:
                        print("RESPUESTA INCORRECTA") 
                        #Ustedes van a manejar una imagen para esto
                        cartas_respuestas[i]["superficie"].fill(COLOR_ROJO)
                        click_error.play()
                    
                    indice +=1
                    
                    if indice == len(lista_preguntas):
                        indice = 0
                        mezclar_lista(lista_preguntas)
                    
                    bandera_respuesta = True
            
    #AGREGAR TEXTO
    #texto_pregunta = fuente_pregunta.render(f"Hola a todos como estan los quiero mucho",False,COLOR_NEGRO)
    #carta_pregunta["superficie"].blit(texto_pregunta,(20,20))
    mostrar_texto(carta_pregunta["superficie"],pregunta_actual["pregunta"],(20,20),fuente_pregunta,COLOR_NEGRO)
    mostrar_texto(cartas_respuestas[0]["superficie"],pregunta_actual["respuesta_1"],(20,20),fuente_respuesta,COLOR_BLANCO)
    mostrar_texto(cartas_respuestas[1]["superficie"],pregunta_actual["respuesta_2"],(20,20),fuente_respuesta,COLOR_BLANCO)
    mostrar_texto(cartas_respuestas[2]["superficie"],pregunta_actual["respuesta_3"],(20,20),fuente_respuesta,COLOR_BLANCO)
    
    #IMPRIMIMOS EN PANTALLA    
    pantalla.fill(COLOR_BLANCO)
    pantalla.blit(carta_pregunta["superficie"],(80,80))
        
    cartas_respuestas[0]["rectangulo"] = pantalla.blit(cartas_respuestas[0]["superficie"],(125,245))#r1
    cartas_respuestas[1]["rectangulo"] = pantalla.blit(cartas_respuestas[1]["superficie"],(125,315))#r2
    cartas_respuestas[2]["rectangulo"] = pantalla.blit(cartas_respuestas[2]["superficie"],(125,385))#r3

    mostrar_texto(pantalla,f"PUNTUACION: {datos_juego['puntuacion']}",(10,10),fuente_texto,COLOR_NEGRO)
    mostrar_texto(pantalla,f"VIDAS: {datos_juego['vidas']}",(10,40),fuente_texto,COLOR_NEGRO)
    
    # pygame.draw.rect(pantalla,COLOR_NEGRO,cartas_respuestas[0]["rectangulo"],5)
    # pygame.draw.rect(pantalla,COLOR_NEGRO,cartas_respuestas[1]["rectangulo"],5)
    # pygame.draw.rect(pantalla,COLOR_NEGRO,cartas_respuestas[2]["rectangulo"],5)
    
    pygame.display.flip()

pygame.quit()