ruta_base = "/home/teo/git1/python_01/Ejercicios_2/"
datos = ruta_base + "Ejercicio_equipo.txt"

lista_pendiente = []
lista_realizado = []


resultado = {}
estado1 = "pendiente"
contador = 0
f = open(datos, "w")

def insertar_tarea():
    pendiente = []
    with open(datos, 'r+') as archivo:
      nueva_tarea = input("Dame una tarea nueva. ")
      while nueva_tarea !='':
        lista_pendiente.append(nueva_tarea)
        nueva_tarea = input("Dame otra tarea: ")

      keys = range(len(lista_pendiente))
      values = lista_pendiente
      for i in keys:
        resultado[i] = values[i]

      for x in resultado:
        pendiente.append(str(x) + ': ' + resultado[x])
      for p in pendiente:
         archivo.write( p + " -> Pendiente" +'\n')

insertar_tarea()

def leer_tarea():
  with open(datos, 'r') as archivo:
    archivo.read()


leer_tarea()

def borrar_tarea():
  pendiente = []
  with open(datos, 'w+') as archivo:
    entrada = int(input("¿Que tarea quieres borrar: "))
    resultado.pop(entrada)

    for x in resultado:
        pendiente.append(str(x) + ': ' + resultado[x])
    for p in pendiente:
         archivo.write( p + " -> Pendiente" +'\n')
    
    # for x in resultado:
    #     archivo.seek(entrada)
    #     archivo.write(str(x) + ': ' + resultado[x] + '\n')


borrar_tarea()

def modificar_tarea():
  pendiente = []
  with open(datos, 'w+') as archivo:
    entrada = int(input("¿Que tarea quieres modificar?: "))
    entrada2 = input("Introduce la nueva tarea: ")
    resultado[entrada] = entrada2
    for x in resultado:
        pendiente.append(str(x) + ': ' + resultado[x])
        print(pendiente)
    for p in pendiente:
         archivo.write( p + " -> Pendiente" +'\n')


modificar_tarea()



def modificar_estado():
  completado = []
  with open(datos, 'w+') as archivo:
    entrada = int(input("¿Que tarea quieres modificar?: "))
    entrada2 = input("Introduce la nueva tarea: ")
    for x in resultado:
      completado.append(str(x) + ': ' + resultado[entrada])
    for p in completado:
         archivo.write( p + " -> Completado" +'\n')
