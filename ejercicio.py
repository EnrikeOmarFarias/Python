
playlist = {} # Diccionario vacio
playlist["canciones"] = [] # Lista vacia de canciones


def app(): # funcion principal

  #Agregar playlist
  agregar_playlist = True
  while agregar_playlist:
    nombre_playlist = input("\r\n como desea nombrar la playlist?\r\n")

    if nombre_playlist:
      playlist["nombre"] = nombre_playlist
      
      agregar_playlist = False #ya tenemos un ombre desactivar el true
      print(playlist)
    #mandar  a llamar la funcion para agregar canciones
    agregar_canciones()

def agregar_canciones():
    agregar_cancion = True #bandera para agregar canciones
    while agregar_cancion:
      #Preguntar al usuarioque cancion desea agregar
      nombre_playlist = playlist["nombre"]
      pregunta = f" \r\n Agrega canciones para la playlist {nombre_playlist}: \r\n"
      pregunta += "Escribe  X para dejar de agregar canciones \r\n"

      cancion = input(pregunta)
      if cancion == "X": #Dejar de agregar canciones
        agregar_cancion = False
        #Mostrar resumen de la playlist
        mostrar_resumen()
      else:
        playlist["canciones"].append(cancion)

def mostrar_resumen():
  nombre_playlist = playlist["nombre"]
  print(f"Playlist: {nombre_playlist} \r\n")
  print("canciones: \r\n ")
  for cancion in playlist["canciones"]:
      print(cancion)

app()