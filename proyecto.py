import os

CARPETA = "contactos/" # Carpeta de contactos
EXTENSION = ".txt" #Extensiones de archivos

#Contactos
class Contactos:
  def __init__(self, nombre, telefono, categoria):
    self.nombre = nombre
    self.telefono = telefono
    self.categoria = categoria


def app():
  #Revisa si la carpeta existe o no
  crear_directorio()
  #Mostrar el menu de opciones
  mostrar_menu()

#Pregunta al usuario la accion a realizar

  preguntar = True
  while preguntar:
    opcion = input("selecione una opcion: \r\n ")
    opcion = int(opcion)

    #Ejecutar las opciones
    if opcion == 1:
      agregar_contacto()
      preguntar  = False
    elif opcion == 2:
      editar_contacto()
      preguntar = False
    elif opcion == 3:
      mostrar_contacto()
      preguntar = False
    elif opcion == 4:
      print("Buscar contacto")
      preguntar = False
    elif opcion == 5:
      print("Eliminar contacto")
      preguntar = False
    else:
      print("Opcion no valida")

def mostrar_contacto():
  archivos = os.listdir(CARPETA)

  archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]

  for archivo in archivos_txt:
    with open(CARPETA + archivo) as contacto:
      for linea in contacto:
        print(linea.rstrip())
      print("\r\n")

def editar_contacto():
  print("Escribe el nombre del contacto a editar")
  nombre_anterior = input("Nombre del contacto que desea editar: \r\n")

  #Revisar si el archivo ya existe antes de editarlo
  existe = existe_contacto(nombre_anterior)

  if existe:
    with open(CARPETA + nombre_anterior + EXTENSION, "w") as archivo:

      # Resto de los campos
      nombre_contacto = input("Agrega el nuevo nombre: \r\n")
      telefono_contacto = input("Agrega el nuevo telefono: \r\n")
      categoria_contacto = input("agrega la nueva categoria : \r\n")

      #Instanciar
    contacto= Contactos(nombre_contacto, telefono_contacto, categoria_contacto)
      
    #Escribir en el archivo
    archivo.write("Nombre: " + contacto.nombre + "\r\n")
    archivo.write("Telefono: " + contacto.telefono + "\r\n")
    archivo.write("Categoria: " + contacto.categoria + "\r\n")

    #Renombrar el archivo
    os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)

    #Mostrar mensaje de exito
    print("\r\n Contacto editado Correctamente \r\n")

  else:
    print("Ese contacto no existe")

  #Reiniciar la aplicacion
  app()

def agregar_contacto():
  print("Escribe los datos para agregar el nuevo Contacto")
  nombre_contacto = input("Nombre del contacto:\r\n")

  #Revisar si el archivo ya existe antes de crearlo

  existe = existe_contacto(nombre_contacto)

  if not existe:
    with open(CARPETA + nombre_contacto + EXTENSION, "w") as archivo:
    
    # Resto de los campos
      telefono_contacto = input("Agrega el telefono: \r\n")
      categoria_contacto = input("Categoria Contacto: \r\n")

    #Instanciar la clase
      contacto = Contactos(nombre_contacto, telefono_contacto, categoria_contacto)

    #Escribir en el archivo
      archivo.write("Nombre: " + contacto.nombre + "\r\n")
      archivo.write("Telefono: " + contacto.telefono + "\r\n")
      archivo.write("Categoria: " + contacto.categoria + "\r\n")

    # Mostrar mensaje de exito
    print("\r\n Contacto creado Correctamente \r\n")
  else:
    print("Ese contacto ya existe")

  # Reiniciar la app
  app()

def mostrar_menu():
    print("Seleccione del menu lo que desee hacer:")
    print("1) Agregar Nuevo Contacto")
    print("2) Ediatar contacto")
    print("3) Ver contactos")
    print("4) Buscar contactos")
    print("5) Eliminar contacto")

def crear_directorio():
  if not os.path.exists(CARPETA):
    os.makedirs(CARPETA) # crear la carpeta
  else:
    print("La carpeta ya existe")

def existe_contacto(nombre):
  return os.path.isfile(CARPETA + nombre + EXTENSION)

app()
