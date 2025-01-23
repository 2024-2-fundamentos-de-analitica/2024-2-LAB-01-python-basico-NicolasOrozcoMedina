"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.
    """
    # Abrir el archivo CSV
    with open('files/input/data.csv', 'r') as archivo:
        # Leer las líneas del archivo
        lineas = archivo.readlines()

    # Procesar las líneas para convertirlas en una lista de datos
    datos = [linea.strip().split('\t') for linea in lineas]

    d = []

    # Recorrer cada fila de los datos
    for fila in datos:
        if len(fila) >= 5:  # Verificar que la fila tiene al menos 5 columnas
            letra = fila[0]  # Columna 1
            elementos_col4 = fila[3].split(",")  # Elementos de la columna 4
            elementos_col5 = fila[4].split(",")  # Elementos de la columna 5

            # Crear la tupla con la letra y las cantidades de elementos
            tupla = (letra, len(elementos_col4), len(elementos_col5))
            d.append(tupla)

    return d


    """
    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
pregunta_10()