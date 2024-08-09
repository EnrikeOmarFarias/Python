
def app():
  archivo= open("archivo.txt", "w")

# generar numeros en un archivo
  for i in range(0, 10):
    archivo.write("Esto es una linea " + str(i) + "\r\n")
#cerrar archivos
  archivo.close()

app()