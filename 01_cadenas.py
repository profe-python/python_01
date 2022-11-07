# Esto es un comentario

# Definimos una variable 

cadena = "En un lugar de la Mancha..."
print(cadena)
print(len(cadena))

print(cadena.capitalize())

print(cadena.swapcase())

print(cadena.replace('la','lo'))

print(cadena.title())

cadena = '1,2,3,4,5,6,7'
trozos = cadena.split(',')
print(trozos)

unida = '. '.join(trozos)
print(unida)
print(cadena + unida)