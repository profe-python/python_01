
numero = int(input('Dime cuantas filas quieres: '))
espacios = numero -1
caracteres = 1

"""
---*---
--***--
-*****-
*******
"""

# print('.'* espacios + '*' * caracteres + '.'* espacios)
# espacios -= 1
# caracteres += 2
# print('.'* espacios + '*' * caracteres + '.'* espacios)
# espacios -= 1
# caracteres += 2
# print('.'* espacios + '*' * caracteres + '.'* espacios)
# espacios -= 1
# caracteres += 2
# print('.'* espacios + '*' * caracteres + '.'* espacios)

for i in range(numero):
    print('\t' * espacios + '*\t' * caracteres + '\t' * espacios)
    espacios -= 1
    caracteres += 2

print()


espacios = 0
caracteres = numero * 2 -1
for i in range(numero):
    print('\t' * espacios + '*\t' * caracteres + '\t' * espacios)
    espacios += 1
    caracteres -= 2


