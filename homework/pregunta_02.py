"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    """
    # Abrir el archivo CSV
    with open('files/input/data.csv', 'r') as archivo:
    # Leer las líneas del archivo
      lineas = archivo.readlines()

    # Procesar las líneas para convertirlas en una lista de datos
    datos = [linea.strip().split(',') for linea in lineas]

    d={}

    for i in datos:
       letra=i[0][0]
       if letra not in d:
          d[letra]=1
       else:
          d[letra]+=1
    return(sorted(d.items()))


    """"


    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """