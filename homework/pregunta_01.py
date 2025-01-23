"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.
    """
    # Abrir el archivo CSV
    with open('files/input/data.csv', 'r') as archivo:
    # Leer las líneas del archivo
      lineas = archivo.readlines()

    # Procesar las líneas para convertirlas en una lista de datos
    datos = [linea.strip().split(',') for linea in lineas]

    sum=0

    for i in datos:
       sum+=int(i[0][2])

    return(sum)
    """
    Rta/
    214

    """