def pide_numero():
    while True:
        try:
            numero = int(input('Inserta un nº entero: '))
            return numero
        except Exception as e:
            continue
    


print(pide_numero())