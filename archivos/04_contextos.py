RUTA_BASE = '/home/teo/git1/python_01/archivos/'
archivo = RUTA_BASE + 'datos_04.txt'

datos = [
    {'nombre': 'Juan','apellido1':'García', 'apellido2': 'Romero', 'edad':22},
    {'nombre': 'María','apellido1':'López', 'apellido2':'Sanchez', 'edad':31},
    {'nombre': 'Miguel','apellido1':'Castillo', 'apellido2':'Garzón', 'edad':44}
]

with open(archivo, 'a+') as f:
    for d in datos:
        cadena = f"{d['nombre']},{d['apellido1']},{d['apellido2']}, {d['edad']}\n"
        f.write(cadena)
    