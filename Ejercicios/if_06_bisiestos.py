numero = 1900

multiplo4 = numero % 4
multiplo100 = numero % 100
multiplo400 = numero % 400

bisiesto = False

if multiplo400 == 0:
    bisiesto = True
elif multiplo100 == 0:
    bisiesto = False
elif multiplo4:
    bisiesto = True

if bisiesto:
    print(f'El año {numero} es bisiesto')
else:
    print(f'El año {numero} NO es bisiesto')
