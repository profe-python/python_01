import pprint

monedas = [500,200,100,50,20,10,5,2,1]
cantidad = 999

numero = cantidad

desglose = {}

for m in monedas:
    desglose[m] = numero // m
    numero =  numero % m

print(desglose)

print ('------------------------------------------')
print(f'La cantidad {cantidad} se desglosa en:')
for clave,valor in desglose.items():
    if valor > 0:
        print(f'{valor} X {clave}')

