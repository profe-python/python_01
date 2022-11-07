base = 5
altura = 4
veces = 4



linea_base = '*' * base
linea_media = '*' + ' ' * (base-2) + '*'

for x in range(veces):
    print(linea_base)

    for i in range(altura - 2):
        print(linea_media)

    print(linea_base)
    print()