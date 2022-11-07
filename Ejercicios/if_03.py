num1 = int(input("Escriba el año actual: "))
num2 = int(input("Escriba un año cualquiera: "))

if num1 == num2:
    print(f"Son el mismo año")
else:
    if num1>num2:
        resultado1= num1 - num2
        print(f"Han pasado {resultado1}")
    else:
        if num2>num1:
            resultado2= num2 - num1
            print(f"Faltan {resultado2} años por llegar")