numero = 100003
if numero % 100_000 == 0:
    print (f'Son {numero//100_000} kilómetros')
else:
    print (f'Son {numero//100_000} kilómetros, {numero%100_000//100} metros y {numero%100} centímetros')