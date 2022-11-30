def limpiar(fila):
    salida = []
    for elem in fila:
        elem = elem.replace('"','').strip()
        elem = elem.replace('\n','')
        salida.append(elem)
    return salida

ruta_base = '/home/teo/git1/python_01/archivos/'
datos = ruta_base + 'hurricanes.csv'


huracanes = []

archivo = open(datos,'r')
cabeceras = archivo.readline()
claves = limpiar(cabeceras.split(','))


for linea in archivo:
    fila = limpiar(linea.split(','))
    d = {}
    for i in range(len(fila)):
        d[claves[i]] = fila[i]
    
    huracanes.append(d)

import pprint

pprint.pprint(huracanes)


    


