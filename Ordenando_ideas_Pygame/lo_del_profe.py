from Constantes import *
import random
import pygame

def mostrar_texto(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, False, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.
    
def mezclar_lista(lista:list) -> None:
    random.shuffle(lista)

def terminar_juego(datos_juego:dict) -> None:
    print("PARTIDA TERMINADA")
    print(f"PUNTUACION TOTAL: {datos_juego["puntuacion"]}")
    datos_juego["usuario"] = input("Ingrese su nombre: ")
    
    #SE GUARDEN LOS RANKINGS -> Esto lo dasarrollan ustedes
    
    print(f"USUARIO: {datos_juego['usuario']}")
    
def reiniciar_estadisticas(datos_juegos:dict) -> None:
    datos_juegos["puntuacion"] = 0
    datos_juegos["vidas"] = CANTIDAD_DE_VIDAS
    
def verificar_respuesta(datos_juego:dict,pregunta_actual:dict,respuesta:int) -> bool:
    if pregunta_actual["respuesta_correcta"] == respuesta:
        datos_juego["puntuacion"] += PUNTUACION_ACIERTOS
        retorno = True
    else:
        #SIN PUNTOS NEGATIVOS
        if datos_juego["puntuacion"] > PUNTUACION_ERROR:
            datos_juego["puntuacion"] -= PUNTUACION_ERROR
        
        #CON PUNTOS NEGATIVOS
        #datos_juego["puntuacion"] -= PUNTUACION_ERROR
        datos_juego["vidas"] -= 1
        retorno = False
    
    return retorno
    
# def jugar_preguntados_consola(datos_juego:dict,lista_preguntas:list[dict]) -> None:
#     #Ciclo del juego
#     indice = 0
#     while datos_juego["vidas"] != 0:
#         print(f"PUNTUACION ACTUAL: {datos_juego["puntuacion"]}")
#         print(f"VIDAS RESTANTES: {datos_juego["vidas"]}\n")
        
#         if indice == len(lista_preguntas):
#             indice = 0
#             mezclar_lista(lista_preguntas)
            
#         pregunta_actual = lista_preguntas[indice]
#         mostrar_pregunta(pregunta_actual)
#         respuesta = pedir_numero("Su respuesta: ","Reingrese su respuesa: (Debe estar 1 y 3)",1,3)
    
#         if verificar_respuesta(datos_juego,pregunta_actual,respuesta):
#             print("RESPUESTA CORRECTA")
#         else:
#             print("RESPUESTA INCORRECTO")
        
#         indice+=1
#         limpiar_consola()