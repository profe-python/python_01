print("Comparador de múltiplos")

numero_1 = int(input("Escribe un número: "))
numero_2 = int(input("Escribe otro número: "))


if numero_1 == 0 or numero_2 == 0:
    print("No se puede dividir entre cero")
else:
    if numero_1 > numero_2:
        resto_1 = numero_1 % numero_2  
        if resto_1 == 0:
            print(f"{numero_1} es múltiplo de {numero_2}")
        else:
            print(f"{numero_1} NO es múltiplo de {numero_2}")
    else:
        resto_2 = numero_2 % numero_1  
        if resto_2 == 0:
            print(f"{numero_2} es múltiplo de {numero_1}")
        else:
            print(f"{numero_2} NO es múltiplo de {numero_1}")


