import csv
import pprint


ruta_base = '/home/teo/git1/python_01/archivos/'
datos = ruta_base + 'ejemplo.csv'

def escribe_writer(archivo):
    with open(archivo,'w') as csvfile:
        escritor = csv.writer(csvfile,delimiter=';')
        escritor.writerow(['Nombre', 'Apellido', 'dni'])
        escritor.writerow(['Paco', 'Gomez', '12345678J'])
        escritor.writerow(['Paco1', 'Gomez1', '12345678J'])
        escritor.writerow(['Paco2', 'Gomez2', '12345678J'])
        escritor.writerow(['Paco3', 'Gomez3', '12345678J'])


#escribe_writer(datos)


def escribe_dict(archivo):
    campos = ['Nombre', 'Apellido', 'dni']
    with open(archivo,'w') as csvfile:
        escritor = csv.DictWriter(csvfile,campos)
        escritor.writeheader()
        escritor.writerow({'Nombre':'Luis', 'Apellido': 'Martin','dni': '98765432K'})


escribe_dict(datos)