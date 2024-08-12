import os

CARPETA = "contactos/"

def app():
  #Revisa si la carpeta existe o no
  crear_directorio()
  #Mostrar el menu de opciones
  mostrar_menu()
def mostrar_menu():
    print("Seleccione del menu lo que desee hacer:")
    print("1) Agregar Nuevo Contacto")
    print("2) Ediatar contacto")
    print("3) ver contactos")
    print("4) Buscar contactos")
    print("5) Eliminar contacto")

def crear_directorio():
  if not os.path.exists(CARPETA):
    os.makedirs(CARPETA) # crear la carpeta
  else:
    print("La carpeta ya existe")


app()
