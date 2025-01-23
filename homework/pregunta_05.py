"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.
    """

    # Abrir el archivo CSV
    with open('files/input/data.csv', 'r') as archivo:
        # Leer las líneas del archivo
        lineas = archivo.readlines()

    # Procesar las líneas para convertirlas en una lista de datos
    datos = [linea.strip().split('\t') for linea in lineas]  # Cambia ',' a '\t' si el delimitador es tabulación

    # Diccionario para almacenar valores agrupados por letra de la columna 1
    d = {}

    # Recorrer cada fila de los datos
    for fila in datos:
        letra = fila[0]  # Columna 1
        valor = int(fila[1])  # Columna 2 (convertir a entero)
        
        # Agregar valor a la lista correspondiente en el diccionario
        if letra not in d:
            d[letra] = []
        d[letra].append(valor)

    # Generar la lista de tuplas con el máximo y mínimo por cada letra
    resultado = [(letra, max(valores), min(valores)) for letra, valores in sorted(d.items())]
    return resultado

    """
    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
pregunta_05()