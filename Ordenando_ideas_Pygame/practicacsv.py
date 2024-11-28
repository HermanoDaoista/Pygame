import os
def mostrar_diccionario(diccionario) -> None:
    for clave,valor in diccionario.items():
        print(f'{clave.title().replace('_',' ')} : {valor}')

def mostra_lista_diccionarios(lista:list)->bool:
    retorno = False
    for elemento in lista:
        retorno = True
        mostrar_diccionario(elemento)
        print('') 
    return retorno           
def crear_diccionario_de_csv(lista_valores:list)-> dict:
    mi_pregunta = {}
    mi_pregunta['pregunta'] = lista_valores[0]
    mi_pregunta['respuesta_1'] = lista_valores[1]
    mi_pregunta['respuesta_2'] = lista_valores[2]
    mi_pregunta['respuesta_3'] = lista_valores[3]
    mi_pregunta['respuesta_4'] = lista_valores[4]
    mi_pregunta['respuesta_correcta'] = lista_valores[5]

    return mi_pregunta
def leer_csv_preguntas(nombre_archivo:str,lista_preguntas:list)-> bool: 
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'r') as archivo:
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

# lista_preguntas = []

# leer_csv_preguntas('lista_random.csv',lista_preguntas)
# mostra_lista_diccionarios(lista_preguntas)

# lista = []
# leer_csv_preguntas('preguntas.csv',lista)

# #crear_diccionario_de_csv(lista)
# mostra_lista_diccionarios(lista)




