import math

entrada = input('¿Quieres calcular el área de un círculo o de un triángulo? Responde C o T: ')
if entrada.upper() == 'C':
    #el área del circulo es pi por el radio al cuadrado
    radio = float(input('Dime el radio de tu círculo: '))
    areacirculo = math.pi * radio ** 2
    mensaje = f'El área de tu círculo es {areacirculo}'
    print(mensaje)
elif entrada.upper() == 'T':
    #el área de un triángulo es la base por la altura dividido entre dos
    base = float(input('Dime la base de tu triángulo: '))
    altura = float(input('Dime la altura de tu triángulo: '))
    areatriangulo1 = base*altura
    areatriangulo2 = areatriangulo1/2
    mensaje2 = f'El área de tu triángulo es {areatriangulo2}'
    print(mensaje2)
else:
    print('Entrada no válida')