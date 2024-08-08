pregunta = "Agrega un numero y te dire si es par o impar \r\n"
pregunta += ' (Escribe "cerrar" para salir de la ejecucuion) \r\n'
preguntar = True

while preguntar:

  numero = input(pregunta)

  if numero == "cerrar":
    preguntar = False
    break
  else:
    numero= int(numero)

    if numero % 2 == 0:
      print(f"el numero es par")
    else:
      print(f"el numero es impar")

