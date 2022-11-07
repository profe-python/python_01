import math
#pedimos los tres datos principales

a = float(input("Escribe el valor del coeficiente a: "))
b = float(input("Escribe el valor del coeficiente b: "))
c = float(input("Escribe el valor del coeficiente c: "))

bcuadrado = b*b
raiz = bcuadrado - 4 * a * c 
a2 = 2 * a

if a == 0:
    if b == 0:
        print("No tiene solución")
    else:
        solucion = -c/b
        print(f'Una Solución {solucion}')
else:
    if raiz >= 0:
        solucionpos = ((-b + math.sqrt(raiz))/a2)
        solucionneg = ((-b - math.sqrt(raiz))/a2)
        if solucionneg == solucionpos:
            print(f'Una solución {solucionpos}')
        else:
            print(f'Las soluciones de la ecuación son {solucionpos} y {solucionneg}')         
    else:
        print('No tiene solución')




