RUTA_BASE = '/home/teo/git1/python_01/archivos/'
archivo = RUTA_BASE + 'datos_03.txt'

datos = [
    {'nombre': 'Juan','apellido1':'García', 'apellido2': 'Romero', 'edad':22},
    {'nombre': 'María','apellido1':'López', 'apellido2':'Sanchez', 'edad':31},
    {'nombre': 'Miguel','apellido1':'Castillo', 'apellido2':'Garzón', 'edad':44}
]

# f = open(archivo, 'w')
# for d in datos:
#     #cadena = d['nombre'] + ',' + d['apellido1'] + ',' + d['apellido2'] + ',' + str(d['edad']) +"\n"
#     cadena = f"{d['nombre']},{d['apellido1']},{d['apellido2']}, {d['edad']}\n"
#     f.write(cadena)
# f.close()
# ------------------------------------
"""
escribe_archivo(nombre, datos)
"""

def escribe_archivo(nombre_archivo, datos):
    f = open(nombre_archivo, 'a+')
    f.write(datos)
    f.close()

c1 = "Juan,García,Romero, 22\n"
c2 = "María,López,Sanchez, 31\n"
c3 = "Miguel,Castillo,Garzón, 44\n"

mi_arch = RUTA_BASE + 'mi_arch.txt'
escribe_archivo(mi_arch, c1)
escribe_archivo(mi_arch, c2)
escribe_archivo(mi_arch, c3)

