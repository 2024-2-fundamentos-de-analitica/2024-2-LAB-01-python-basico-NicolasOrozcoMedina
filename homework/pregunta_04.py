"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.
    """
    # Abrir el archivo CSV
    with open('files/input/data.csv', 'r') as archivo:
    # Leer las líneas del archivo
      lineas = archivo.readlines()

    # Procesar las líneas para convertirlas en una lista de datos
    datos = [linea.strip().split(',') for linea in lineas]
    d={}
    for i in datos:
       a=i[0][9]
       b=i[0][10]
       if a+b not in d:
          d[a+b]=1
       else:
          d[a+b]+=1
    return(sorted(d.items()))

    """""
    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """