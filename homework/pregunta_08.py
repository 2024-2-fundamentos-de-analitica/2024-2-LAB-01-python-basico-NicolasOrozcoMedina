"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.
    """
    # Abrir el archivo CSV
    with open('files/input/data.csv', 'r') as archivo:
        # Leer las líneas del archivo
        lineas = archivo.readlines()

    # Procesar las líneas para convertirlas en una lista de datos
    datos = [linea.strip().split('\t') for linea in lineas]

    # Diccionario para almacenar listas de letras asociadas por valor de la columna 2
    d = {}

    # Recorrer cada fila de los datos
    for fila in datos:
        letra = fila[0]  # Columna 1
        valor = int(fila[1])  # Columna 2 (convertir a entero)

        # Agregar letra a la lista correspondiente al valor
        if valor not in d:
            d[valor] = []
        if letra not in d[valor]:
           d[valor].append(letra)
        d[valor].sort()   
        

    # Crear una lista de tuplas ordenada por los valores de la columna 2
    resultado = sorted(d.items())
    return resultado
    """

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """
pregunta_08()