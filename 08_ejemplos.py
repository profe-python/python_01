import time

usr = 'Teo'

tiempo = input(f'Cuantos minutos quieres, {usr}:> ')
tiempo_int = int(tiempo)
time.sleep(tiempo_int)
print('El pollo está listo')