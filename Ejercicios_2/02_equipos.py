import random 
import pprint

alumnos = [
    'Javi', 
    'Jose',
    'Miguel', 
    'A.Muñoz',
    'Ana',
    'A.Sánchez',
    'Luciano', 
    'Juan', 
    'Pablo',
    'Dani',
    'Pedro',
    'Adrián',
    'Pablo G.']


    

def crea_equipos(gente,miembros):
    """
    Crear equipos con los miembros aleatorios de la lista 'gente' 
    y con tantas personas por equipo como diga el parámetro 'miembros'
    """
    salida = []
    num_equipos = len(gente) // miembros
    offset = 0

    random.shuffle(gente)
    for i in range(num_equipos):
        salida.append([gente[offset],gente[offset + 1]])
        offset += 2

    return salida


#print(crea_equipos(alumnos,3))

def migue(gente, miembros):
    if len(gente) < miembros:
        return gente
    
    if miembros == 0:
        return []

    random.shuffle(gente)

    num_grupos = len(gente) // miembros
    listas = []

    for i in range(num_grupos):
        equipo = []
        for j in range(miembros):
            equipo.append(gente.pop())
        listas.append(equipo)
    
    for p in range(len(gente)):
        listas[p].append(gente[p])

    return listas


pprint.pprint(migue(alumnos, 3))








    # 1. Calcular el número de equipos 
    # 2. Crear las listas y llenarlas ALEATORIAMENTE
    # 3. Asignar las personas restantes a los equipos sin que se repitan
    
    # PROBLEMAS SIN RESOLVER
    # - --------------------
    # No sabemos como elegir aleatoriamente las personas
    # No sabemos como evitar que se repitan
    # No sabemos como añadir las personas que sobran
    # 

# crea_equipos(alumnos, 3)

