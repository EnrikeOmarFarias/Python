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
      print("Editar contacto")
      preguntar = False
    elif opcion == 3:
      print("Ver contacto")
      preguntar = False
    elif opcion == 4:
      print("Buscar contacto")
      preguntar = False
    elif opcion == 5:
      print("Eliminar contacto")
      preguntar = False
    else:
      print("Opcion no valida")


def agregar_contacto():
  print("Escribe los datos para agregar el nuevo Contacto")
  nombre_contacto = input("Nombre del contacto:\r\n")

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

  
app()
