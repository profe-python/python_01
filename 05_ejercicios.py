# Entrada: Pedimos un número al usuario

# Salida:
#   Imprimir: "El doble de <20> son <40>"
#             "El cuadrado de <20> son <400>"    


numero = input('Introduce un número: ')
entero = int(numero)

doble = 2 * entero
cuadrado = entero * entero

print('El doble de ' + numero + ' es ' + str(doble))
print('El cuadrado de ' + numero + ' es ' + str(cuadrado))

mensaje = f'El doble de {numero} es {doble}'
print(mensaje)