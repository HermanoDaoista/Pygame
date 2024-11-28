from Constantes import *
import random
import pygame
import os
import json
import operator
def mostrar_texto(surface, text, pos, font, color=pygame.Color('black')):
    """funcion magica hecha por el profe

    Args:
        surface (_type_): _description_
        text (_type_): _description_
        pos (_type_): _description_
        font (_type_): _description_
        color (_type_, optional): _description_. Defaults to pygame.Color('black').
    """
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
    """reordena una lista aleatoriamente
    la usamos para cambiar la pregunta en pantalla

    Args:
        lista (list): _description_
    """

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
    """esta funcion resulve la logica de sumar puntos si la respues es correcta
    y restar si es incorrecta

    Args:
        datos_juego (dict): _description_
        pregunta_actual (dict): _description_
        respuesta (int): _description_

    Returns:
        bool: _description_
    """
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

def crear_diccionario_de_csv(lista_valores:list)-> dict:
    """esta funcion nos sirve para a cada indice de la lista que es leida de archivo
    csv se le asigne una clave de diccionario

    Args:
        lista_valores (list): _description_

    Returns:
        dict: _description_
    """
    mi_pregunta = {}
    mi_pregunta['pregunta'] = lista_valores[0]
    mi_pregunta['respuesta_1'] = lista_valores[1]
    mi_pregunta['respuesta_2'] = lista_valores[2]
    mi_pregunta['respuesta_3'] = lista_valores[3]
    mi_pregunta['respuesta_4'] = lista_valores[4]
    mi_pregunta['respuesta_correcta'] = int(lista_valores[5])

    return mi_pregunta
def leer_csv_preguntas(nombre_archivo:str,lista_preguntas:list)-> bool: 
    """esta funcion sirve para leer nuestro archivo csv, comprueba si el archivo existe en el path
    que le damos, lo abre y reemplaza en cada linea los \n con comas, se transforma en una lista 
    que luego pasaamos a dict. esos dict lo agregamos a la lista quedando una list[dict]

    Args:
        nombre_archivo (str): _description_
        lista_preguntas (list): _description_

    Returns:
        bool: retorna booleano
    """
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'r',encoding='utf-8') as archivo:
            archivo.readline()
            for linea in archivo:
                lineaux = linea.replace('\n','')
                lista_valores = lineaux.split(',')
                mi_pregunta = crear_diccionario_de_csv(lista_valores)
                lista_preguntas.append(mi_pregunta)
                
        retorno = True
    else:
        retorno = False    
    return retorno


def mostrar_texto_margen(surface, text, font, color, rect, padding=10):
    """
    Renderiza texto dentro de un área rectangular en la superficie.

    Args:
        surface: Superficie de Pygame donde se dibujará el texto.
        text: Texto a mostrar.
        font: Fuente de Pygame.
        color: Color del texto.
        rect: Rectángulo (x, y, ancho, alto) que define el área legible.
        padding: Espaciado interno del texto con respecto al rectángulo.
    """
    words = [line.split(' ') for line in text.splitlines()]  # Divide el texto en líneas y palabras.
    space_width = font.size(' ')[0]  # Ancho del espacio.
    x, y = rect[0] + padding, rect[1] + padding  # Posición inicial con padding.
    max_width = rect[2] - padding * 2  # Ancho máximo para texto dentro del área.
    max_height = rect[3] - padding * 2  # Altura máxima para texto dentro del área.

    for line in words:
        line_width = 0
        for word in line:
            word_surface = font.render(word, True, color)
            word_width, word_height = word_surface.get_size()

            # Salta a la siguiente línea si el texto excede el ancho disponible.
            if x + word_width > rect[0] + max_width:
                x = rect[0] + padding
                y += word_height

            # Deja de renderizar si el texto excede el área visible en altura.
            if y + word_height > rect[1] + max_height:
                return

            surface.blit(word_surface, (x, y))
            x += word_width + space_width  # Avanza la posición x.

        # Reinicia x y avanza a la siguiente línea.
        x = rect[0] + padding
        y += font.get_linesize()  # Usa el alto de línea de la fuente.

def crear_botones(imagen_boton:pygame.Surface,tamanio_boton:tuple) ->dict:
    """crea un objeto del tipo surface a partir de una imagen y un tama;io

    Args:
        imagen_boton (pygame.Surface): _description_
        tamanio_boton (tuple): _description_

    Returns:
        dict: _description_
    """

    boton = {}
    boton['superficie'] = pygame.transform.scale(imagen_boton, tamanio_boton)  # Escalar la imagen al tamaño deseado
    boton['rectangulo'] = boton['superficie'].get_rect()
    return boton

def guardar_ranking(ranking, archivo="partidas.json"):
    """guarda el diccionario ranking en un archivo json

    Args:
        ranking (_type_): _description_
        archivo (str, optional): _description_. Defaults to "partidas.json".
    """
   
    with open(archivo, 'w') as file:
        json.dump(ranking, file, indent=4)

def ordenar_por_numero(ranking:dict, operador, clave: str):
    """Burbujeo fallido use sort()

    Args:
        ranking (dict): _description_
        operador (_type_): _description_
        clave (str): _description_

    Returns:
        _type_: _description_
    """
   
    for i in range(len(ranking) - 1):
        for j in range(i+1,len(ranking)):
            if operador(ranking[i][clave], ranking[j][clave]):
                auxiliar = ranking[i]
                ranking[i] = ranking[j]
                ranking[j] = auxiliar
        
    return ranking   

def cargar_ranking(archivo:json):
    """abre y cierra el archivo json que contiene los ranking

    Args:
        archivo (_type_): _description_

    Returns:
        _type_: _description_
    """
    if os.path.exists(archivo):
        with open(archivo, 'r') as f:
            return json.load(f)
    else:
        return []
   

def guardar_ranking(archivo:json, ranking:dict):
    """garda el ranking en un json

    Args:
        archivo (_type_): _description_
        ranking (_type_): _description_
    """
    with open(archivo, 'w') as f:
        json.dump(ranking, f, indent=4) 



def actualizar_ranking(ranking:dict, usuario:dict, puntuacion:dict,fecha:str)->dict:
    """esta funcion resuelve la logica de ordenar el diccionario, luego comrpueba
    si 'puntuacion' es mayor que el menor en la lista, si es asi lo agrega.Tambien lo agrega si el
    len de mi dict es menor a 10, verifica que nombre no exista, si existe y puntuacion es mayor
    lo sobreescribe. Vuelve a ordenar, hace un slicing  desde el indice 0 hasta el 10(que no lo incluye)

    Args:
        ranking (dict): _description_
        usuario (dict): _description_
        puntuacion (dict): _description_
        fecha (str): _description_

    Returns:
        dict: _description_
    """
    
    ranking.sort(key=operator.itemgetter('puntuacion'), reverse=True)
   
    if len(ranking) >= 10 and puntuacion <= ranking[9]['puntuacion']:

        return ranking
       

    for registro in ranking:
        if registro['usuario'] == usuario:
            
            if puntuacion > registro['puntuacion']:
                registro['puntuacion'] = puntuacion
            break
    else:
        
        ranking.append({'usuario': usuario, 'puntuacion': puntuacion, 'fecha': fecha})

    ranking.sort(key=operator.itemgetter('puntuacion'), reverse=True)
    return ranking[:10]

def pausar_musica():
    """estas funciones de una sola linea tienen la funcion de hacerme capas de manipular el volumen
    general desde cualquier modelo que quiera
    """
    pygame.mixer.music.pause()

def desmutear_musica():
    """estas funciones de una sola linea tienen la funcion de hacerme capas de manipular el volumen
    general desde cualquier modelo que quiera
    """
    pygame.mixer.music.unpause()

def mutear_musica():
    """estas funciones de una sola linea tienen la funcion de hacerme capas de manipular el volumen
    general desde cualquier modelo que quiera
    """
    pygame.mixer.music.set_volume(0)

def restaurar_volumen(volumen):
    """estas funciones de una sola linea tienen la funcion de hacerme capas de manipular el volumen
    general desde cualquier modelo que quiera
    """
    pygame.mixer.music.set_volume(volumen)

def cargar_musica(pista:str,volumen_real:float):
    """carga la musica desde una pista especificada y la setea un volumen

    Args:
        pista (str): _description_
        volumen_real (float): _description_
    """
    pygame.mixer.music.load(pista)
    pygame.mixer.music.set_volume(volumen_real)
    pygame.mixer.music.play(-1)    
   

def subir_volumen(datos_del_juego:dict):
    """sube el volumen del juego

    Args:
        datos_del_juego (dict): _description_
    """
    if datos_del_juego['volumen_musica'] < 100:
        SONIDO_PLOC.play()
        datos_del_juego['volumen_musica'] += 5
    else:
        SONIDO_ERROR.play() 
def restar_volumen(datos_del_juego:dict):
    """resta volumen al juego

    Args:
        datos_del_juego (dict): _description_
    """
    if datos_del_juego['volumen_musica'] < 100:
        SONIDO_PLOC.play()
        datos_del_juego['volumen_musica'] -= 5
    else:
        SONIDO_ERROR.play() 
