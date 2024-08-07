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