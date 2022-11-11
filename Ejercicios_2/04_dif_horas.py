from horas_minutos import hora_segundos_3

"""
Escribir una función que reciba dos horas en formato 'hh:mm:ss'
Debe devolver la diferencia entre ellas en formato 'hh:mm:ss'
"""

def dif_horas(inicio, fin):
    diferencia = abs(hora_segundos_3(fin) - hora_segundos_3(inicio))
    h = diferencia // 3600
    m = diferencia % 3600 // 60
    s = diferencia % 3600 % 60

    return f'{h:02d}:{m:02d}:{s:02d}'


print(dif_horas('20:00:00','19:59:00'))


"""
1. Pasar inicio y fin a segundos usando hora_segundos
2. Restar los valores 
3. Calcular horas, minutos y segundos
4. Devolver la cadena

"""
