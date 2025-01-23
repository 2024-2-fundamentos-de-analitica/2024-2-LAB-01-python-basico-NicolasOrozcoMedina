"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.
    """
    # Abrir el archivo CSV
    with open('files/input/data.csv', 'r') as archivo:
        # Leer las líneas del archivo
        lineas = archivo.readlines()

    # Procesar las líneas para convertirlas en una lista de datos
    datos = [linea.strip().split('\t') for linea in lineas]

    d = {}

    # Recorrer cada fila de los datos
    for fila in datos:
            
            elementos_col4 = fila[3].split(",")  # Elementos de la columna 4
            numero=fila[1]
            for i in elementos_col4:
                if i not in d:
                      d[i]=0
                d[i]+=int(numero)
        

    return d

    """

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
pregunta_11()
