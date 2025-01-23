"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.
    """
    # Abrir el archivo CSV
    with open('files/input/data.csv', 'r') as archivo:
        lineas = archivo.readlines()

    valores = {}

    # Procesar cada línea
    for linea in lineas:
        # Obtener la columna 5 (última columna) y dividir las entradas separadas por coma
        columna5 = linea.strip().split('\t')[-1]
        items = columna5.split(',')

        for item in items:
            clave, valor = item.split(':') 
            if clave not in valores:
                valores[clave]=1
            else:
                valores[clave]+=1
    return valores

    """

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
pregunta_09()