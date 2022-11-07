import pprint


#Diccionarios

d ={
    'uno': 'Primero',
    'dos': 'Segundo',
    'hola@gmail.com': 'Miguel'

}

d['tres'] = 'Tercero'

# print(d['uno'])
# print(d['hola@gmail.com'])
# del(d['tres'])
# d.clear()
# print(list(d))

# ------------------------

coches = {
    '1234-FRD':'Opel Corsa',
    '0987-SDR': 'Ford Fiesta',
    '1929-PLK': 'Ford Kuga'
}

coches['7777-SDB'] = 'Mercedes Clase A'

pprint.pprint(coches)






