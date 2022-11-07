#Tipos mutables
numero = 0

numero = 1

cadena = 'hola' 
cadena = 'adios'

#Tipos inmutables

#entrada
#cadena = 'Esto es un experimento con cadenas'

#salida
# cadena = 'Esto es un EXPERIMENTO con cadenas'

# 1. Encontrar la palabra 'experimento' --> 11
# 2. Cortar la cadena en 3 pedazos
# 3. Poner 'experimento' en mayúsculas --> upper()
# 4. Unir las cadenas 

# --------------------------
cadena = 'Esto es un truco del almendruco de experimento con cadenas'
palabra = 'almendruco'
longitud = len(palabra)
pto1 = cadena.find(palabra)
pto2 = pto1 + longitud


parte1 = cadena[:pto1]
parte2 = palabra.upper()
parte3 = cadena[pto2:]

resultado = parte1 + parte2 + parte3

print(resultado)