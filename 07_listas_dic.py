import pprint

mi_lista = [1,2,3,4,'hola',True,['a','b','c']]
mi_lista.append('otro')
mi_lista.extend([7,8,9])
mi_lista.insert(4,'nuevo dato')

mi_lista = mi_lista + ['k','l','m'] + [1,4,7]
x = mi_lista.pop()
print('X: ',x)

lector = mi_lista[5]
print('Lector: ',lector)

print(mi_lista)


# ############# Tuplas ###################

mi_tupla = (1,2,3,19,2,1)

largo = len(mi_tupla)
elem = mi_tupla.count(0)
elem3= mi_tupla[3]
print('Largo: ',largo)
print('Elem: ', elem)
print('Tercero: ',elem3)
print(list(mi_tupla))


# ################ Diccionarios ################

mi_dict = {
    '1':1, 
    '4':16,
    '2':4, 
    '3':9,      
    '5':25
}
mi_dict['6'] = 36
print (mi_dict['6'])




persona1 = {
    'nombre' : 'Paco_1',
    'dni': '12344567L'
}
persona2 = {
    'nombre' : 'Paco_2',
    'dni': '12344567L'
}
personas = {
    1: persona1,
    2: persona2
}


pprint.pprint(personas)




