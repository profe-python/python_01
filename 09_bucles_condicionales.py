"""
numero = int(input('Dime un numerito: '))

if numero == 0:
    print('El número es cero')
else:
    if numero > 0:
        print('El número  es mayor que cero')
    else:
        print('El número es menor que cero')
"""
# ########### Operadores ##################
"""
Aritméticos

+
-
*
/
** Exponente
// División entera
%  Módulo (resto de la división entera)
-----------------------
Comparación
>
<
==
!= Distinto
>=
<=
------------------------
Asignación o incremento

+= 
-=
*=
/=
//=
%=
**=

"""
"""
numero = int(input('Dime un numerito: '))

if numero % 2 == 0:
    print(f'El número {numero}  es par')
else:
    print(f'El número {numero}  es impar')
"""


numero = float(input('Dime un numerito: '))
resultado = ''

if numero < 5:
    resultado = 'SUSPENSO'
else:
    if numero < 7:
        resultado = 'APROBADO'
    else:
        if numero < 9: 
            resultado = 'NOTABLE'
        else:
            resultado = 'SOBRESALIENTE'

print(resultado)



