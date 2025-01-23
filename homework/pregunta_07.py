"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 1 y 2. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.
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
        d[valor].append(letra)

    # Crear una lista de tuplas ordenada por los valores de la columna 2
    resultado = sorted(d.items())
    return resultado

pregunta_07()
