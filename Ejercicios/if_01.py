print ("Divisor de números")
num1 = input("Escriba el dividendo:")
dividendo = int (num1)
num2 = input("Escriba el divisor:")
divisor = int (num2)

if divisor == 0:
    print ("No se puede dividir por 0")
else:
    cociente = dividendo // divisor
    resto = dividendo % divisor
    if resto == 0:
        print ("La división es exacta")
        print ("Cociente: ",cociente)
    else:
        print ("La división no es exacta")
        print ("Cociente: ",cociente)
        print ("Resto: ",resto)
  