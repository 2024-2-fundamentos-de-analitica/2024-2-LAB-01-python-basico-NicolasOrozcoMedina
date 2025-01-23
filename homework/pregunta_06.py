"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.
    """
    # Abrir el archivo CSV
    with open('files/input/data.csv', 'r') as archivo:
        lineas = archivo.readlines()

    # Diccionario para almacenar los valores mínimo y máximo para cada clave
    valores = {}

    # Procesar cada línea
    for linea in lineas:
        # Obtener la columna 5 (última columna) y dividir las entradas separadas por coma
        columna5 = linea.strip().split('\t')[-1]
        items = columna5.split(',')

        for item in items:
            clave, valor = item.split(':')  # Dividir en clave y valor
            valor = int(valor)  # Convertir valor a entero

            # Actualizar el diccionario con los valores mínimos y máximos
            if clave not in valores:
                valores[clave] = [valor, valor]  # Inicializar con valor como min y max
            else:
                valores[clave][0] = min(valores[clave][0], valor)  # Actualizar min
                valores[clave][1] = max(valores[clave][1], valor)  # Actualizar max

    # Convertir los resultados a una lista de tuplas ordenada por clave
    resultado = [(clave, min_max[0], min_max[1]) for clave, min_max in sorted(valores.items())]
    return resultado

    """"

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
pregunta_06()