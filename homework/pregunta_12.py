"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.
    """
    # Abrir el archivo CSV
    with open('files/input/data.csv', 'r') as archivo:
        lineas = archivo.readlines()

    d = {}

    # Procesar cada línea
    for linea in lineas:
        # Obtener la columna 5 (última columna) y dividir las entradas separadas por coma
        columna5 = linea.strip().split('\t')[-1]
        items = columna5.split(',')
        letra=linea[0]

        for item in items:
            clave, valor = item.split(':')  # Dividir en clave y valor
            valor = int(valor)  # Convertir valor a entero
            if letra not in d:
                d[letra]=0
            d[letra]+=valor
    return d
        

    """

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
pregunta_12()