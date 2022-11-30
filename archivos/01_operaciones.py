# r, w, a, 
# w+(si existe se borra, si no se crea),
# r+(si no existe da error) , 
# a+(si existe se añade por el final), 
# b

ruta_base = '/home/teo/git1/python_01/archivos/'
ruta_imagenes = ruta_base + 'images/'

archivo = open(ruta_base + 'pruebas.txt','r')
numeros = []

for linea in archivo:
    numeros.append(int(linea))

archivo.close()
print(numeros)


