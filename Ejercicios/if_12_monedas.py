numero = 17_342

billete500 = numero // 500
resto500 = numero % 500 

billete200 = resto500 // 200
resto200 = resto500 % 200

billete100 = resto200 // 100
resto100 = resto200 % 100

billete50 = resto100 // 50
resto50 = resto100 % 50

billete20 = resto50 // 20
resto20 = resto50 % 20

billete10 = resto20 // 10
resto10 = resto20 % 10

billete5 = resto10 // 5
resto5 = resto10 % 5

moneda2 = resto5 // 2
resto2 = resto5 % 2

mensaje = f"El monto {numero} te lo darán en {billete500} billetes de 500 \n"
print(mensaje)


#print(resto500)