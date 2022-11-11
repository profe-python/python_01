"""
tenemos un texto y hay que 
    - limpiar el texto de signos de puntuación
    - eliminar palabras no relevantes (3 letras o menos)
    - contabilizar palabras del texto en un diccionario
    - devolver el diccionario
"""
"""
PENSAR:
OK 1.  Pasar a minúsculas
OK 1b. Quitar signos de puntuación
2.  Ignorar palabras de 3 letras o menos
3.  Dividir la cadena por palabras
4.  Procesar la cadena
"""

import string

def frecuencias(texto):
    salida = {}

    texto = texto.lower()
    puntuacion = list(string.punctuation)
    for p in puntuacion:
        texto = texto.replace(p,'')

    palabras = texto.split()
    for palabra in palabras:
        if len(palabra) >3:
            if salida.get(palabra) == None:
                salida[palabra] = 1
            else:
                salida[palabra] += 1
    
    return salida
    
    
    






txt = """Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like)."""

import pprint
pprint.pprint(frecuencias(txt))
