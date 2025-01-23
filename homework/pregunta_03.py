"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.
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
          d[letra]=0
          d[letra]+=int(i[0][2])
       else:
          d[letra]+=int(i[0][2])
       print(d)
    return(sorted(d.items()))

    """""
    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """