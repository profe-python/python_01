"""
Hacer una función que reciba una hora en formato hh:mm:ss.
Debe devolver la cantidad de segundos de dicha hora.

"""

def hora_segundos(cadena_hora):
    trozos_hora = cadena_hora.split(':')
    valores = []
    for i in trozos_hora:
        i = int(i)
        valores.append(i)
    
    segundos_hora = valores[0] * 3600
    segundos_minutos = valores[1] * 60
    suma = segundos_hora + segundos_minutos + valores[2]
    return suma


def hora_segundos_2(cadena_hora):
    horas = cadena_hora[0:2]
    horas = int(horas)
    minutos = cadena_hora[3:5]
    minutos = int(minutos)
    segundos = cadena_hora[6:8]
    segundos = int(segundos)

    salida = horas * 3600 + minutos * 60 + segundos
    return salida

def hora_segundos_3(cadena_hora):
    return int(cadena_hora[0:2]) * 3600 + int(cadena_hora[3:5]) * 60 + int(cadena_hora[6:8])

    


#print(hora_segundos_3('23:24:24')) # 84264