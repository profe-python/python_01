n1=int(input('Dime un numerito: '))
n2=int(input('Dime otro numerito quillo: '))
if n1==n2:
    print('Los números son iguales')
else:
    if n1>n2:
        print(f'El número mayor es el {n1} y el número menor es el {n2}')
    else:
        print(f'El número menor es el {n1} y el mayor es el {n2}')
    