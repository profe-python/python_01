# ax+b = 0

# x = -b/a

valor_a = float(input('Introduce un numero: '))
valor_b = float(input('Introduce otro numero: '))

if valor_a == 0 and valor_b == 0:
    print('Todos los números son solución')

elif valor_a == 0:
    print('No tiene solución')


else:
    solucion = -valor_b / valor_a
    print(f'La solucion de la ecuación es: {solucion}')