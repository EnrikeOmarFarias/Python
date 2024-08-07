def bienvenida(nombre, mensaje):
  print(f"Hola {nombre} {mensaje}")

bienvenida("Tito", "Bienvenido al curso!!!")

def suma(a, b = 0):
  print(a + b)

suma(2, 100)

#estoy agregando un comentario

lenguajes = ["python", "java", "javaScript"]
print(lenguajes)
print(lenguajes[1])

#ordenar los elementos
lenguajes.sort()
print(lenguajes)

# acceder a un elemento de un texto
aprendiendo = f"estoy aprendiendo {lenguajes[2]}"
print(aprendiendo)

#modificando valores de un arreglo
lenguajes[2] = "php"
print(lenguajes)

#agregar elementos a un arreglo
lenguajes.append("ruby")
print(lenguajes)

#eliminar de una lista
del lenguajes[1]
print(lenguajes)

lenguajes.pop
print(lenguajes)

#eliminar por nombre
lenguajes.remove("php")
print(lenguajes)

#iterador

for lenguajes in lenguajes:
  print(f"estoy aprendiendo {lenguajes}")

# for que escriba numero
for numero in range(0, 10):
  print(numero)

  #if en python

balance = 0
if balance > 0:
  print("Puedes pagar")
else:
  print("saldo insuficiente")

  #evaluar un boolean

  usuario_ok = False
  usuario_admin = False

  if usuario_ok == True:
    if usuario_admin:
      print("acceso total")
    else:
      print("Tienes acceso al sistema")
  else:
    print("debes iniciar sesion")


ocupacion = "estudiant"

if ocupacion == "estudiante":
  print("Tienes 50% de descuento")
elif ocupacion == "Jubilado":
  print("Tienes 75% de descuento")
else:
  print("tienes que pagar el 100% GATOOOOO")


# And y or

usuario_logueado = True
usuario_admin = True

if usuario_admin and usuario_logueado:
  print("administrador")
elif usuario_logueado:
  print("Acceso al sistema")
else:
  print("debes iniciar sesion")

# condicinales

for lenguaje in lenguajes:
  print(lenguaje)

#objeto o diccionarios

cancion = {
  "artista" : "pibes chorros",
  "cancion" : "duraznito",
  "año" : 1996,
}
print(cancion["artista"])

# mezclar con un string
artista = cancion["artista"]
print(f"estoy escuchando {artista}")

# iniciar un diccionario vacio

jugador = {}
print(jugador)
# se une un jugador
jugador["nombre"] = "juan"
jugador["puntaje"] = 0
print(jugador)
# incrementando el puntaje
jugador["puntaje"] = 100
print(jugador)
#aceder a un valor
print(jugador.get("consola", "No existe ese valor"))
# iterar en el diccionario
for llave, valor in jugador.items():
  print(llave)
  print(valor)

#eliminar jugador y puntaje
del jugador["nombre"]
del jugador["puntaje"]
print(jugador)

# input

nombre = input("¿Cual es tu nombre? \r\n")

print(f"Hola {nombre}")


edad = input("cual es tu edad? \r\n")
#convertir edad string a entero
edad = int(edad)

if edad >= 18:
  print("ya puedes votar")
else:
  print("Aun no puedes votar")

#Mezclarlo con operadores

numero = input("Agrega un numero y te dire si es par o impar \r\n")

numero = int(numero)

if numero % 2 == 0:
  print(f"el numero es par")
else:
  print(f"el numero es impar")
  