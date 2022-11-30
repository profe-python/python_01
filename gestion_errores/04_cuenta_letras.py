

"""
Hacer un programa que pida al usuario una serie de caracteres.
Cuando termine le debe mostrar una lista con las vocales y otra con las consonantes, 
además de decirle cuantas hay de cada una.
Los caracteres que no son letras se descartan.
"""

consonantes = "bcdfghjklmnpqrstvwxyzñ"
vocales = 'aeiouáéíóú'

lista_consonantes = []
lista_vocales = []

while True:
    letra = input('Dime una letra: ')
    if letra == '':
        break
    if letra.lower() in consonantes:
        lista_consonantes.append(letra)
    elif letra.lower() in vocales:
        lista_vocales.append(letra)

print(f'Consonantes: {len(lista_consonantes)}')
print(lista_consonantes)

print(f'Vocales: {len(lista_vocales)}')
print(lista_vocales)



